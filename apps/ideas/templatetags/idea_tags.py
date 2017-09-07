import json

from django import forms, template
from django.contrib.contenttypes.models import ContentType
from django.utils.html import format_html

from adhocracy4.ratings.models import Rating

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


@register.simple_tag(takes_context=True)
def react_supports(context, idea):
    request = context['request']
    user = request.user

    contenttype = ContentType.objects.get_for_model(idea)

    permission = '{ct.app_label}.rate_{ct.model}'.format(ct=contenttype)
    has_support_permission = user.has_perm(permission, idea)

    if user.is_authenticated():
        authenticated_as = user.username
    else:
        authenticated_as = None
    user_support = Rating.objects.filter(
        content_type=contenttype, object_pk=idea.pk, creator=user.pk).first()
    if user_support:
        user_support_value = user_support.value
        user_support_id = user_support.pk
    else:
        user_support_value = None
        user_support_id = -1

    attributes = {
        'contentType': contenttype.pk,
        'objectId': idea.pk,
        'authenticatedAs': authenticated_as,
        'supports': idea.positive_rating_count,
        'userSupport': user_support_value,
        'userSupportId': user_support_id,
        'isReadOnly': not has_support_permission
    }

    return format_html(
        '<span data-ae-widget="supports"'
        '      data-attributes="{attributes}" ></span>',
        attributes=json.dumps(attributes),
        pk=idea.pk
    )
