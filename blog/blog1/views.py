from django.views.generic import ListView, DetailView, FormView

from blog.blog1.models import Post, PostComment
from blog.main.forms import CommentForm
from blog.main.views import PostRelatedViewMixin


class BlogPostListView(PostRelatedViewMixin, ListView):
    model = Post
    queryset = Post.objects.filter(approved=True).order_by('date')
    template_name = 'blog-1/posts.html'
    paginate_by = 25


class BlogPostView(PostRelatedViewMixin, DetailView, FormView):
    model = Post
    template_name = 'blog-1/post.html'
    form_class = CommentForm
    comment_model = PostComment

    def form_valid(self, form):
        self.comment_model.objects.create(
            user=self.request.user,
            comment=form.cleaned_data.get('comment'),
            approved=True,
            post=self.model.objects.get(id=self.kwargs.get('pk'))
        )

        return super(BlogPostView, self).form_valid(form)

    def get_success_url(self):
        return self.request.path
