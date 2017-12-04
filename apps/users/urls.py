from django.conf.urls import url

from . import USERNAME_REGEX, views

urlpatterns = [
    url(
        '^profile/(?P<username>{})/$'.format(USERNAME_REGEX[1:-1]),
        views.ProfileView.as_view(),
        name='profile',
    ),
    url(
        '^accounts/edit/$'.format(USERNAME_REGEX[1:-1]),
        views.EditProfileView.as_view(),
        name='edit_profile',
    ),
    url(
        '^accounts/notifications/$'.format(USERNAME_REGEX[1:-1]),
        views.NotificationsView.as_view(),
        name='notifications',
    ),
]
