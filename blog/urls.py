from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.BlogPostsListView.as_view(), name='blog'),
    path('blog/<slug>/', views.BlogPostView.as_view(), name='blog_post'),
    path('blog-category/<slug>/', views.BlogCategoryView.as_view(), name='blog_category'),
]
