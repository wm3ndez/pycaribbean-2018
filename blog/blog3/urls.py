from django.urls import path

from blog.blog3.views import BlogPostListView, BlogPostView

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blog-3'),
    path('post/<int:pk>/', BlogPostView.as_view(), name='post-3')
]
