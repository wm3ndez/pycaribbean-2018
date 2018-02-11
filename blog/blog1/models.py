from django.db import models

from blog.main.models import PostAbstract, CommentAbstract


class Post(PostAbstract):
    pass


class PostComment(CommentAbstract):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
