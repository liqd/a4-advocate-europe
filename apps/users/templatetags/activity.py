from django import template

register = template.Library()


def _ignore_action(action):
    return action.type == 'follows' and not action.obj.enabled


@register.simple_tag
def filter_actions(actions):
    return list(filter(lambda a: not _ignore_action(a), actions))
