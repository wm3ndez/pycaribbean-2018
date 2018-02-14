from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32)
    parent = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag = models.CharField(max_length=40)

    def __str__(self):
        return '#%s' % self.tag


class PostAbstract(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=60)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(null=True, blank=True)
    approved = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
    views = models.PositiveIntegerField(default=0)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        self.save()

    @property
    def score(self):
        comments_score = self.concrete_model.postcomment_set.count() * 0.1
        return comments_score + self.views * 0.01

    class Meta:
        abstract = True


class CommentAbstract(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        abstract = True
