from django.conf.urls import url

from . import views
from .forms import (ApplicantSectionForm, CollaborationCampSectionForm,
                    CommunitySectionForm, IdeaSectionForm, ImpactSectionForm,
                    PartnersSectionForm)

urlpatterns = [
    url(r'create/module/(?P<slug>[-\w_]+)/$',
        views.IdeaSketchCreateWizard.as_view(
            [ApplicantSectionForm, PartnersSectionForm,
             IdeaSectionForm, ImpactSectionForm,
             CollaborationCampSectionForm,
             CommunitySectionForm]), name='idea-sketch-create'),
    url(r'^(?P<slug>[-\w_]+)/$',
        views.IdeaSketchDetailView.as_view(), name='idea-sketch-detail'),
    url(r'list/export/$', views.IdeaSketchExportView.as_view(),
        name='idea-sketch-export'),
    url(r'^$',
        views.IdeaSketchListView.as_view(), name='idea-sketch-list')

]
