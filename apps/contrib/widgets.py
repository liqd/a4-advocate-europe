from itertools import chain

import django_filters
from django.db.models.fields import BLANK_CHOICE_DASH
from django.forms import TextInput
from django.forms.widgets import flatatt
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _


class DropdownLinkWidget(django_filters.widgets.LinkWidget):
    label = None
    right = False
    template = 'advocate_europe_contrib/widgets/dropdown_link.html'

    def get_option_label(self, value, choices=()):
        option_label = BLANK_CHOICE_DASH[0][1]

        for v, label in chain(self.choices, choices):
            if str(v) == value:
                option_label = label
                break

        if option_label == BLANK_CHOICE_DASH[0][1]:
            option_label = _('All')

        return option_label

    def render(self, name, value, attrs=None, choices=()):
        all_choices = list(chain(self.choices, choices))

        if len(all_choices) <= 1:
            return ''

        if value is None:
            value = all_choices[0][0]

        _id = attrs.pop('id')
        final_attrs = flatatt(self.build_attrs(attrs))
        value_label = self.get_option_label(value, choices=choices)

        options = super().render(name, value, attrs={
            'class': 'dropdown-menu',
            'aria-labelledby': _id,
        }, choices=choices)

        return render_to_string(self.template, {
            'options': options,
            'id': _id,
            'attrs': final_attrs,
            'value_label': value_label,
            'label': self.label,
            'right': self.right,
        })


class TextInputWidget(TextInput):
    label = None
    right = False
    template = 'advocate_europe_contrib/widgets/text_input.html'

    def get_context(self, name, value, attrs=None):
        # import pdb; pdb.set_trace()
        context = super().get_context(name, value, attrs)
        return context

    def render(self, name, value, attrs=None):

        if value is None:
            value = ''

        _id = attrs.pop('id')

        # context = self.get_context(name, value, attrs)

        return render_to_string(self.template, {
            'id': _id,
            'value_label': value,
            'label': self.label,
            'right': self.right,
        })
