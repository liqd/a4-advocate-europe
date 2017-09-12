from django import template

register = template.Library()


@register.assignment_tag()
def get_identifier(item):
    return id(item)
