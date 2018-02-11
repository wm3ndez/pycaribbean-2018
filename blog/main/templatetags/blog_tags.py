from django import template

register = template.Library()


@register.inclusion_tag('pagination.html')
def paginate(page_obj):
    return {'page_obj': page_obj}
