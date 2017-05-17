from django.conf.urls import url

from . import views
from .forms import (ApplicantSectionForm, CollaborationCampSectionForm,
                    CommunitySectionForm, FinanceAndDurationSectionForm,
                    IdeaSectionForm,
                    ImpactSectionForm, PartnersSectionForm)

urlpatterns = [
    url(r'create/module/(?P<slug>[-\w_]+)/$',
        views.IdeaSketchCreateWizard.as_view(
            [ApplicantSectionForm, PartnersSectionForm,
             IdeaSectionForm, ImpactSectionForm,
             CollaborationCampSectionForm,
             CommunitySectionForm]), name='idea-sketch-create'),
    url(r'^(?P<slug>[-\w_]+)/$',
        views.IdeaDetailView.as_view(), name='idea-detail'),
    url(r'^(?P<slug>[-\w_]+)/edit/$',
        views.IdeaSketchEditView.as_view(), name='idea-sketch-update'),
    url(r'^(?P<slug>[-\w_]+)/proposal/$',
        views.ProposalCreateWizard.as_view(
            [ApplicantSectionForm, PartnersSectionForm,
             IdeaSectionForm, ImpactSectionForm,
             FinanceAndDurationSectionForm, CommunitySectionForm]
        ), name='idea-sketch-add-proposal'),
    url(r'^(?P<slug>[-\w_]+)/edit/(?P<form_number>[\d]+)/$',
        views.IdeaSketchEditView.as_view(), name='idea-sketch-update-form'),
    url(r'list/export/$', views.IdeaSketchExportView.as_view(),
        name='idea-sketch-export'),
    url(r'^$',
        views.IdeaSketchListView.as_view(), name='idea-sketch-list')

]
