from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from blog.main.models import PostAbstract, CommentAbstract, Category, Tag


class Post(PostAbstract):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='b3_posts'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='b3_posts'
    )
    approved = models.BooleanField(default=False, db_index=True)
    featured = models.BooleanField(default=False, db_index=True)
    tags = models.ManyToManyField(Tag, related_name='b3_posts')


class PostComment(CommentAbstract):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='b3_comments'
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    approved = models.BooleanField(default=True, db_index=True)


@receiver(post_save, sender=PostComment)
def notify_users(sender, instance, *args, **kwargs):
    import django_rq
    from blog.main.utils import send_email_notifications_async

    queue = django_rq.get_queue('high')
    queue.enqueue(
        send_email_notifications_async,
        instance.post.id,
        instance.user.id,
        instance.user.email
    )
