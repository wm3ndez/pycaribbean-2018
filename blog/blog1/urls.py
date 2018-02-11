from django.urls import path

from blog.blog1.views import BlogPostListView

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blog-1')
]
