from django.urls import path

from blog.blog2.views import BlogPostListView, BlogPostView

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blog-2'),
    path('post/<int:pk>/', BlogPostView.as_view(), name='post-2')
]
