from django import template

register = template.Library()


@register.assignment_tag
def get_range(number, listcount):
    if number < 3:
        return range(1, 6)
    elif number > listcount - 2:
        return range(listcount-4, listcount+1)
    else:
        return range(number-2, number+3)


@register.assignment_tag
def combined_url_parameter(request_query_dict, **kwargs):
    combined_query_dict = request_query_dict.copy()
    for key in kwargs:
        combined_query_dict.setlist(key, [kwargs[key]])
    encoded_parameter = '?' + combined_query_dict.urlencode()
    return encoded_parameter


@register.assignment_tag
def concat_strings(*args):
    """concatenate strings"""
    concat_str = ''
    for string in args:
        concat_str += str(string)
    return concat_str


@register.assignment_tag
def get_absolute_uri(request, obj):
    return request.build_absolute_uri(obj)
