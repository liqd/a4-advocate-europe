from django.conf.urls import url

from . import views
from .forms import (ApplicantSectionForm, CommunitySectionForm,
                    FinanceAndDurationSectionForm, FinishForm,
                    IdeaChallengeCampSectionForm, IdeaSectionForm,
                    ImpactSectionForm, NetworkForm, PartnersSectionForm,
                    SelectionCriteriaSectionForm)

urlpatterns = [
    url(r'create/module/(?P<slug>[-\w_]+)/$',
        views.IdeaSketchCreateWizard.as_view(
            [ApplicantSectionForm, PartnersSectionForm,
             IdeaSectionForm, ImpactSectionForm,
             IdeaChallengeCampSectionForm,
             CommunitySectionForm, FinishForm]), name='idea-sketch-create'),
    url(r'^archived/(?P<slug>[-\w_]+)/$',
        views.IdeaSketchArchivedDetailView.as_view(),
        name='idea-sketch-archived-detail'),
    url(r'^(?P<slug>[-\w_]+)/$',
        views.IdeaDetailView.as_view(), name='idea-detail'),
    url(r'^(?P<slug>[-\w_]+)/edit/$',
        views.IdeaSketchEditView.as_view(), name='idea-sketch-update'),
    url(r'^(?P<slug>[-\w_]+)/edit/(?P<form_number>[\d]+)/$',
        views.IdeaSketchEditView.as_view(), name='idea-sketch-update-form'),
    url(r'^(?P<slug>[-\w_]+)/proposal/$',
        views.ProposalCreateWizard.as_view(
            [ApplicantSectionForm, PartnersSectionForm,
             IdeaSectionForm, ImpactSectionForm, SelectionCriteriaSectionForm,
             NetworkForm, FinanceAndDurationSectionForm,
             CommunitySectionForm, FinishForm]
        ), name='idea-sketch-add-proposal'),
    url(r'^(?P<slug>[-\w_]+)/proposal/edit/$',
        views.ProposalEditView.as_view(), name='proposal-update'),
    url(r'^(?P<slug>[-\w_]+)/proposal/edit/(?P<form_number>[\d]+)/$',
        views.ProposalEditView.as_view(), name='proposal-update-form'),
    url(r'list/export/$', views.IdeaExportView.as_view(),
        name='idea-export'),
    url(r'^$',
        views.IdeaListView.as_view(), name='idea-sketch-list')

]
