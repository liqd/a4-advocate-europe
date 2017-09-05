from django.template import Library, Node, TemplateSyntaxError
from django.utils import translation

register = Library()


class TransNode(Node):
    def __init__(self, nodelist, lc):
        self.nodelist = nodelist
        self.lc = lc

    def render(self, context):
        with translation.override(self.lc):
            return self.nodelist.render(context)


def force_translation(parser, token):
    """ Parse force_translation template tag.

    .. code:: django
      {% force_translation 'en' %}
          {{ _('Will always be english') }}
      {% endforce_translation %}
    """
    try:
        nodelist = parser.parse(('endforce_translation',))
        parser.delete_first_token()
        tag_name, lc = token.split_contents()
    except ValueError:
        raise TemplateSyntaxError(
            '{} tag requires arguments'.format(token.contents.split()[0])
        )
    if not (lc[0] == lc[-1] and lc[0] in ('"', "'")):
        raise TemplateSyntaxError(
            '{} locale should be in quotes'.format(tag_name)
        )
    return TransNode(nodelist, lc[1:-1])


register.tag('force_translation', force_translation)
