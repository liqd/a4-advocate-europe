from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        views.IdeaSketchListView.as_view(), name='ideasketch-list'),
]
