from django.conf.urls import url

from . import USERNAME_REGEX, views


urlpatterns = [
    url(
        '^profiles/(?P<username>{})$'.format(USERNAME_REGEX[1:-1]),
        views.ProfileView.as_view(),
        name='profile',
    ),
    url(
        '^accounts/edit/$'.format(USERNAME_REGEX[1:-1]),
        views.EditProfileView.as_view(),
        name='edit_profile',
    ),
]
