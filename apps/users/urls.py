from django.conf.urls import url

from . import USERNAME_REGEX, views


urlpatterns = [
    url(
        '^profiles/(?P<username>{})$'.format(USERNAME_REGEX[1:-1]),
        views.ProfileView.as_view(),
        name='profile',
    ),
]
