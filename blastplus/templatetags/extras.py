"""
Module extending django's functionality
"""

from django import template

register = template.Library()


@register.filter
def get_at_index(l, index):
    """Filter in template, returns object at index.   """
    return l[index]
