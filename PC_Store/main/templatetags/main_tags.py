from django import template

register = template.Library()

from ..models import Post

@register.filter
def get_class_name(value):
    return value.__class__.__name__