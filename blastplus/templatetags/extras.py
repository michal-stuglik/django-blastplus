"""
Module extending django's functionality
"""

from django import template

register = template.Library()

@register.filter
def get_at_index(list, index):
    """Filter in template, returns object at index.   """
    return list[index]