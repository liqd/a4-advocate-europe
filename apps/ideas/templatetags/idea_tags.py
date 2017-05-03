from django import forms, template


register = template.Library()


@register.filter(name='is_multi_select_checkbox')
def is_checkbox(bound_field):
    widget = bound_field.field.widget.__class__
    return widget is forms.CheckboxSelectMultiple
