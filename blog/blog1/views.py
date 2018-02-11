from django.views.generic import ListView

from blog.blog1.models import Post


class BlogPostListView(ListView):
    model = Post
    queryset = Post.objects.filter(approved=True).order_by('date')
    template_name = 'blog-1/posts.html'
    paginate_by = 25
