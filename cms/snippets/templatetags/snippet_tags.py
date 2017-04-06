from django import template
from django.utils import translation

from cms.snippets.models import NavigationMenu

register = template.Library()


@register.assignment_tag(takes_context=False)
def load_site_menu(menu_name):
    menu = NavigationMenu.objects.filter(menu_name=menu_name)

    if menu:
        return menu[0].menu_items.all()
    else:
        return None


@register.simple_tag
def get_translated_field(block, field):
    current_language = translation.get_language()
    if block.value[field + '_' + current_language]:
        return block.value[field + '_' + current_language]
    else:
        return block.value[field + '_en']
