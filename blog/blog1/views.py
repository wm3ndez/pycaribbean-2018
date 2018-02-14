from django.views.generic import ListView, DetailView

from blog.blog1.models import Post
from blog.main.views import PostRelatedViewMixin


class BlogPostListView(PostRelatedViewMixin, ListView):
    model = Post
    queryset = Post.objects.filter(approved=True).order_by('date')
    template_name = 'blog-1/posts.html'
    paginate_by = 25


class BlogPostView(PostRelatedViewMixin, DetailView):
    model = Post
    template_name = 'blog-1/post.html'
