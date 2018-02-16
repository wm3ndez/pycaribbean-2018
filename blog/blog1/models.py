from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from blog.main.models import PostAbstract, CommentAbstract
from blog.main.utils import send_email_notifications


class Post(PostAbstract):
    pass


class PostComment(CommentAbstract):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


@receiver(post_save, sender=PostComment)
def notify_users(sender, instance, *args, **kwargs):
    send_email_notifications(instance)
