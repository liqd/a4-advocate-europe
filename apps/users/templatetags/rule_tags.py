from django import template

from adhocracy4.modules.models import Module

register = template.Library()


@register.assignment_tag
def get_module(module_slug):
    return Module.objects.get(slug=module_slug)
