from django import template

from .. import sanatize_next

register = template.Library()


@register.inclusion_tag(
    'advocate_europe_users/indicator_menu.html', takes_context=True)
def userindicator_menu(context):
    context['redirect_field_value'] = sanatize_next(context['request'])
    return context
