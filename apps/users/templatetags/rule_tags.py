from django import template

from adhocracy4.modules.models import Module

register = template.Library()


@register.simple_tag
def get_modules():
    return Module.objects.all()
