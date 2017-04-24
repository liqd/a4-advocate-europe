from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        views.ideasketchlist, name='idea-sketch-list'),
]

# views.IdeaSketchListView.as_view()
