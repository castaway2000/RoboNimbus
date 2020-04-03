from django.shortcuts import HttpResponse, HttpResponseRedirect, get_object_or_404
from django.views import generic
from .models import BlogPost, BlogCategory
from django.conf import settings


class BlogPostsListView(generic.ListView):
    model = BlogPost
    queryset = BlogPost.objects.all_published()
    paginate_by = settings.BLOG_PAGE_SIZE
    ordering = ["-order_index"]
    template_name = "blog/blog_posts.html"

    def get_context_data(self, **kwargs):
        context = super(BlogPostsListView, self).get_context_data(**kwargs)
        context["page"] = "blog"
        context["object_featured_list"] = BlogPost.objects.all_featured()
        return context


class BlogPostView(generic.DetailView):
    model = BlogPost
    template_name = "blog/post_details.html"

    def get_context_data(self, **kwargs):
        context = super(BlogPostView, self).get_context_data(**kwargs)
        context["page"] = "blog"
        return context


class BlogCategoryView(generic.DetailView):
    model = BlogCategory

    def get_context_data(self, **kwargs):
        context = super(BlogCategoryView, self).get_context_data(**kwargs)
        context["page"] = "blog"
        return context