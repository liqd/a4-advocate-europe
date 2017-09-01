from django import template
from django.utils.html import format_html

register = template.Library()


@register.simple_tag()
def react_follows(followable):
    return format_html(
        '<span data-ae-widget="follows"'
        '      data-followable={pk}></span>',
        pk=followable.pk
    )
