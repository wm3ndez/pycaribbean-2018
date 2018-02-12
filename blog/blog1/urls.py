from django.urls import path

from blog.blog1.views import BlogPostListView, BlogPostView

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blog-1'),
    path('post/<int:pk>/', BlogPostView.as_view(), name='post-1')
]
