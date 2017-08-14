from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create/idea/(?P<slug>[-\w_]+)/$',
        views.JourneyEntryCreateView.as_view(),
        name='journey-entry-create'),
    url(r'^(?P<pk>[-\w_]+)/edit/$',
        views.JourneyEntryUpdateView.as_view(),
        name='journey-entry-update'),
    url(r'^(?P<pk>[-\w_]+)/delete/$',
        views.JourneyEntryDeleteView.as_view(),
        name='journey-entry-delete'),
]
