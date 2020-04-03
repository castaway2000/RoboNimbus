from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from unidecode import unidecode
from utils.images_resizing import optimize_size
from utils.uploadings import UploadToPathAndRename
from crequest.middleware import CrequestMiddleware
from django.contrib.auth.models import User
from django.contrib.sitemaps import ping_google



class BlogCategory(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    slug = models.SlugField(blank=True, null=True, unique=True)
    order_index = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'BlogCategory'
        verbose_name_plural = 'BlogCategories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(BlogCategory, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})


class PostManager(models.Manager):

    def all_published(self):
        return self.filter(is_active=True).order_by('-order_index', 'id')

    def all_featured(self):
        return self.filter(is_active=True, is_featured=True).order_by('-order_index', 'id')


class BlogPost(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    title = models.CharField(max_length=256, blank=True, null=True, default=None)
    slug = models.SlugField(blank=True, null=True, unique=True)
    text = models.TextField(blank=True, null=True, default=None)
    preview_text = models.TextField(blank=True, null=True, default=None)
    category = models.ForeignKey(BlogCategory, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to=UploadToPathAndRename("image"), blank=True, null=True, default=None)
    image_small = models.ImageField(upload_to=UploadToPathAndRename("image_small"), blank=True, null=True,
                                    default="blog/post_default_small.jpg")
    image_medium = models.ImageField(upload_to=UploadToPathAndRename("image_medium"), blank=True, null=True,
                                     default="blog/post_default_medium.jpg")
    image_large = models.ImageField(upload_to=UploadToPathAndRename("image_large"), blank=True, null=True,
                                     default="blog/post_default_large.jpg")
    order_index = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = PostManager()

    def __str__(self):
        return '%s' % self.title

    def __init__(self, *args, **kwargs):
        super(BlogPost, self).__init__(*args, **kwargs)

        self._original_fields = {}
        for field in self._meta.get_fields(include_hidden=True):
            try:
                self._original_fields[field.name] = getattr(self, field.name)
            except:
                pass

    class Meta:
        verbose_name = 'BlogPost'
        verbose_name_plural = 'BlogPosts'

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        current_request = CrequestMiddleware.get_request()
        if current_request:
            user = current_request.user
            if not self.pk:
                self.user = user

        if self.image and ((self._original_fields["image"] != self.image) or not self.image_large
                           or not self.image_medium or not self.image_small):
            self.image_small = optimize_size(self.image, "small")
            self.image_medium = optimize_size(self.image, "medium")
            self.image_large = optimize_size(self.image, "large")

        super(BlogPost, self).save(*args, **kwargs)
        ping_google()

    def get_absolute_url(self):
        return reverse("blog_post", kwargs={"slug": self.slug})