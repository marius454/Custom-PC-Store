from django import template

register = template.Library()

from ..models import Post

@register.filter
def get_class_name(value):
    return value.__class__.__name__

@register.filter
def get_name(value):
    return value.__name__