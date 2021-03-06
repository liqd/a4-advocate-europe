from django.urls import Resolver404, resolve
from django.utils.http import is_safe_url
from django.utils.translation import ugettext_lazy as _

default_app_config = 'apps.users.apps.Config'

USERNAME_REGEX = r'^[\w]+[ \w.@+\-]*$'
USERNAME_INVALID_MESSAGE = _('Enter a valid username. This value may contain '
                             'only letters, digits, spaces and @/./+/-/_ '
                             'characters. It must start with a digit or a '
                             'letter.')


def _get_account_url_names():
    from allauth.account import urls
    return tuple([url.name for url in urls.urlpatterns])


def sanatize_next(request):
    """
    Get appropriate next value for the given request
    """
    try:
        url_name = resolve(request.path).url_name
    except Resolver404:
        url_name = '__invalid_url_name__'

    if url_name in _get_account_url_names():
        nextparam = request.GET.get('next') or request.POST.get('next') or '/'
        if is_safe_url(nextparam, allowed_hosts={request.get_host()}):
            next = nextparam
        else:
            next = '/'
    else:
        next = request.get_full_path()
    return next
