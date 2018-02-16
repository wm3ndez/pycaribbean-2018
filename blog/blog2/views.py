from django.views.generic import ListView

from blog.blog1.views import BlogPostView as PostView
from blog.blog2.models import Post, PostComment
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
    template_name = 'blog-2/posts.html'
    paginate_by = 25


class BlogPostView(PostView):
    model = Post
    comment_model = PostComment
    template_name = 'blog-2/post.html'
