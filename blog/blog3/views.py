from django.views.generic import ListView, DetailView

from blog.blog3.models import Post
from blog.main.views import PostRelatedViewMixin


class BlogPostListView(PostRelatedViewMixin, ListView):
    model = Post
    queryset = Post.objects.select_related(
        'author', 'category',
    ).prefetch_related(
        'postcomment_set', 'tags'
    ).filter(
        approved=True
    ).order_by('date')
    template_name = 'blog-3/posts.html'
    paginate_by = 25


class BlogPostView(PostRelatedViewMixin, DetailView):
    model = Post
    template_name = 'blog-3/post.html'
