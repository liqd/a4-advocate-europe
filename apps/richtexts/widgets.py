from django import forms
from django.forms.utils import flatatt
from django.utils.html import escape
from django.utils.safestring import mark_safe


class Editor(forms.Textarea):

    def use_required_attribute(self, *args):
        return False

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''

        final_attrs = {
            'class': 'richtext',
            'style': 'background: #f3f3f3; border: 1px solid #d8d8d8;'
        }

        if attrs:
            final_attrs.update(attrs)

        html = [
            '<a href class="image-link">add image</a>',
            '<div{!s}>{!s}</div>'.format(flatatt(final_attrs), escape(value))
        ]
        return mark_safe('\n'.join(html))

    @property
    def media(self):
        return forms.Media(
            css={
                'all': [
                    '//cdn.quilljs.com/1.3.2/quill.bubble.css',
                    'richtexts/editor.css',
                ],
            },
            js=[
                '//cdn.quilljs.com/1.3.2/quill.js',
                'richtexts/modal-workflow.js',
                'richtexts/editor.js',
            ])
