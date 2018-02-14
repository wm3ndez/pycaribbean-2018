from django import template
from django.db.models import F, Count, FloatField
from django.db.models.functions import Cast

register = template.Library()


@register.inclusion_tag('pagination.html')
def paginate(page_obj):
    return {'page_obj': page_obj}


@register.inclusion_tag('popular-posts.html')
def popular_posts(PostModel, slice=5):
    Post = PostModel.__class__
    posts = Post.objects.prefetch_related('postcomment_set')
    posts = posts.annotate(
        post_score=Cast(F('views') * 0.01 + Count('postcomment') * 0.1, FloatField()),
    ).order_by('-post_score')

    return {'posts': posts[:slice]}


@register.inclusion_tag('featured-posts.html')
def featured_posts(PostModel, slice=5):
    Post = PostModel.__class__
    posts = Post.objects.filter(featured=True)
    return {'posts': posts[:slice]}
