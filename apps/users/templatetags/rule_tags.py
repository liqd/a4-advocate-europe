from django import template

from adhocracy4.modules.models import Module

register = template.Library()


@register.assignment_tag
def get_modules():
    return Module.objects.all()
