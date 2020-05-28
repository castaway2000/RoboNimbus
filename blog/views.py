from django.shortcuts import HttpResponse, HttpResponseRedirect, get_object_or_404
from django.views import generic
from .models import BlogPost, BlogCategory
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class BlogPostsListView(generic.ListView):
    model = BlogPost
    queryset = BlogPost.objects.all_published()
    paginate_by = settings.BLOG_PAGE_SIZE

    ordering = ["-order_index"]
    template_name = "blog/blog_posts.html"

    def get_context_data(self, **kwargs):
        blog_posts = BlogPost.objects.filter(**kwargs).order_by("-id").values()

        page = self.request.GET.get('page', 1)
        paginator = Paginator(blog_posts, 10)
        try:
            blog_posts = paginator.page(page)
            index = blog_posts.number - 1
            max_index = len(paginator.page_range)
            start_index = index - 5 if index >= 5 else 0
            end_index = index + 5 if index <= max_index - 5 else max_index
            page_range = paginator.page_range[start_index:end_index]
        except PageNotAnInteger:
            blog_posts = paginator.page(1)
        except EmptyPage:
            blog_posts = paginator.page(paginator.num_pages)

        context = super(BlogPostsListView, self).get_context_data(**kwargs)
        context["page"] = "blog"
        context["page_range"] = page_range
        context['last_in_range'] = page_range[-1]
        context["object_featured_list"] = BlogPost.objects.all_featured()
        context["blog_posts"] = blog_posts
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