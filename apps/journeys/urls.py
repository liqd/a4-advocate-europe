from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<slug>[-\w_]+)/$',
        views.JourneyEntryCreateView.as_view(),
        name='journey-entry-create'),
]
