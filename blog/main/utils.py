from django.contrib.auth.models import User
from django.core.mail import send_mail, mail_admins

from blog.blog3.models import Post


def send_email_notifications_async(post, user, user_email):
    send_mail(
        "New comment on post %s" % Post.objects.get(id=post),
        "Hi %s,\nYour comment was accepted." % User.objects.get(id=user),
        "user@example.com",
        [user_email or "user@example.com"]
    )

    mail_admins(
        "New comment on post %s" % post,
        "Hi Williams, %s commented on a post." % user
    )


def send_email_notifications(post_comment):
    send_mail(
        "New comment on post %s" % post_comment.post,
        "Hi %s,\nYour comment was accepted." % post_comment.user,
        "user@example.com",
        [post_comment.user.email or "user@example.com"]
    )

    mail_admins(
        "New comment on post %s" % post_comment.post,
        "Hi Williams, %s commented on a post." % post_comment.user
    )
