from collections import namedtuple

from django import template
from django.core.cache import cache
from django.db.models import F, Count, FloatField
from django.db.models.functions import Cast

from blog.main.models import Category

register = template.Library()
COMMENTS_FACTOR = 0.1
VIEWS_FACTOR = 0.01
CategoryTree = namedtuple('CategoryTree', ['id', 'name', 'children'])


@register.inclusion_tag('pagination.html')
def paginate(page_obj):
    return {'page_obj': page_obj}


@register.inclusion_tag('popular-posts.html')
def popular_posts(PostModel, slice=5):
    Post = PostModel.__class__
    posts = Post.objects.prefetch_related('postcomment_set')

    score = F('views') * VIEWS_FACTOR + Count('postcomment') * COMMENTS_FACTOR
    score = Cast(score, FloatField())
    posts = posts.annotate(post_score=score).order_by('-post_score')

    return {'posts': posts[:slice]}


@register.inclusion_tag('featured-posts.html')
def featured_posts(PostModel, slice=5):
    Post = PostModel.__class__
    posts = Post.objects.filter(featured=True)
    return {'posts': posts[:slice]}


@register.inclusion_tag('category-tree.html')
def category_tree():
    def get_children(category):
        return [CategoryTree(c.id, c.name, get_children(c))
                for c in category.category_set.all()]

    # Parent categories
    categories = Category.objects.filter(parent__isnull=True)
    tree = []
    for category in categories:
        tree.append(CategoryTree(category.id, category.name, get_children(category)))

    return {'tree': _render_category_tree(tree)}


@register.inclusion_tag('category-tree.html')
def cached_category_tree():
    # @cached
    def get_children(category):
        return [CategoryTree(c.id, c.name, get_children(c))
                for c in category.category_set.all()]

    # Parent categories
    categories = Category.objects.filter(
        parent__isnull=True
    ).prefetch_related('category_set')
    tree = []
    for category in categories:
        children = cache.get('category-%s' % category.id)
        if children is None:
            children = get_children(category)
            cache.set(
                'category-%s' % category.id,
                children,
                timeout=60 * 60 * 3  # 3 hours
            )

        tree.append(CategoryTree(category.id, category.name, children))

    return {'tree': _render_category_tree(tree)}


def _render_category_tree(tree):
    html = '<ul>'
    for node in tree:
        html += '<li><a href="#">{}</a>{}</li>' \
            .format(node.name, _render_category_tree(node.children))
    html += '</ul>'
    return html
