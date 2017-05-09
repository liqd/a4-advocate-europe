from django.conf.urls import url

from . import models, views


def invite_urls(invite_model):
    view_name = invite_model.__name__.lower()

    return [
        url(
            r'^invites/{}/(?P<invite_token>[-\w_]+)/$'.format(view_name),
            views.InviteDetailView.as_view(),
            name='{}-detail'.format(view_name)
        ),
        url(
            r'^invites/{}(?P<invite_token>[-\w_]+)/accept/$'.format(view_name),
            views.InviteUpdateView.as_view(),
            name='{}-update'.format(view_name)
        ),
    ]


urlpatterns = invite_urls(models.IdeaSketchInvite)
