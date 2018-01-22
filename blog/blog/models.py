from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32)
    parent = models.ForeignKey('self', on_delete=models.PROTECT)

    class Meta:
        abstract = True


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=60)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField()
    published = models.DateTimeField()
    approved = models.BooleanField(default=False)

    class Meta:
        abstract = True
