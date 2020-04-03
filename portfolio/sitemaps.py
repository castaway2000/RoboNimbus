from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import BlogPost


class StaticSitemap(Sitemap):
    """Reverse 'static' views for XML sitemap."""
    priority = 1.0
    changefreq = 'yearly'

    def items(self):
        return ['home', 'tos', 'privacy']

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):
    priority = 0.7
    changefreq = "weekly"

    def items(self):
        return BlogPost.objects.all()
