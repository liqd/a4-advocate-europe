from wagtail.snippets.models import register_snippet

from .categories import Category
from .navigation_menus import NavigationMenu

register_snippet(Category)
register_snippet(NavigationMenu)
