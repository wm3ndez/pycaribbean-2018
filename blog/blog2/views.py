from django.views.generic import ListView, DetailView

from blog.blog2.models import Post


class BlogPostListView(ListView):
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


class BlogPostView(DetailView):
    model = Post
    template_name = 'blog-2/post.html'
