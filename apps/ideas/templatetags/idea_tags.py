from django import forms, template


register = template.Library()


@register.filter(name='is_multi_select_checkbox')
def is_checkbox(bound_field):
    widget = bound_field.field.widget.__class__
    return widget is forms.CheckboxSelectMultiple


@register.assignment_tag
def count_active_filter(request_query_dict):
    count = 0
    for key, value in request_query_dict.items():
        if value and key != 'ordering':
            count += 1
    return count
