from django.core.paginator import Paginator
from django.http import Http404
from django.utils.http import is_safe_url
from django.views import generic

from adhocracy4.exports.mixins import VirtualFieldMixin
from adhocracy4.modules.models import Module
from adhocracy4.phases.models import Phase
from adhocracy4.rules.discovery import NormalUser

from .models import Idea, IdeaSketch, Proposal
from .paginators import DeltaFirstPagePaginator


class IdeaMixin(generic.detail.SingleObjectMixin):
    model = Idea

    def dispatch(self, request, *args, **kwargs):
        self.idea = self.get_object()
        self.object = self.idea
        return super().dispatch(request, *args, **kwargs)


class ModuleMixin(generic.detail.SingleObjectMixin):
    model = Module

    def dispatch(self, request, *args, **kwargs):
        self.module = self.get_object()
        self.object = self.module
        return super().dispatch(request, *args, **kwargs)


class MultiFormEditMixin():
    """
    Allows to edit a large model in smaller parts.

    There should be two routes for this view, one with an aditional form_number
    parameter and one without. For each provided form a (sub)-view is created,
    the user can navigate between the views by submitting them and setting the
    next parameter. It is required that each form can be validated/stored
    independently from the others.
    """
    form_classes = ()
    form_number_keyword = 'form_number'

    def dispatch(self, request, *args, **kwargs):
        form_number = self.kwargs.get(self.form_number_keyword, '0')
        if not form_number.isdecimal():
            raise Http404

        form_number = int(form_number)
        self.form_number = form_number
        if form_number < 0 or len(self.form_classes) <= form_number:
            raise Http404

        self.form_class = self.form_classes[form_number]
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        next = self.request.POST.get('next')

        # only allow same host as request
        allowed_hosts = {self.request.get_host()}

        if next and is_safe_url(next, allowed_hosts=allowed_hosts):
            return next
        else:
            return self.request.path


class CtaPaginatorMixin:
    """
    Leaves space for cta tile if cta_permission is given for current user.
    """
    cta_permission = 'advocate_europe_ideas.add_ideasketch'

    @property
    def cta_object(self):
        phase = Phase.objects.active_phases().last()

        if phase:
            return phase.module

    @property
    def is_cta_enabled(self):
        if self.cta_object:
            has_or_would_have_perm = (
                self.request.user.has_perm(
                    self.cta_permission,
                    self.cta_object
                ) or
                NormalUser().would_have_perm(
                    self.cta_permission,
                    self.cta_object
                )
            )
            return has_or_would_have_perm
        else:
            return False

    def get_paginator(self, *args, **kwargs):
        if self.is_cta_enabled:
            self.paginator_class = DeltaFirstPagePaginator
        else:
            self.paginator_class = Paginator
        return super().get_paginator(*args, **kwargs)


class ExportMultiModelIdeaFieldsMixin(VirtualFieldMixin):
    exclude = None

    def get_virtual_fields(self, virtual):
        ideasketch_fields = IdeaSketch._meta.get_fields()
        proposal_fields = Proposal._meta.get_fields()

        fields = set(ideasketch_fields + proposal_fields)
        exclude = self.exclude if self.exclude else []

        for field in fields:
            if field.concrete \
                    and not (field.one_to_one
                             and field.remote_field.parent_link) \
                    and field.name not in exclude \
                    and field.name not in virtual:
                virtual[field.name] = str(field.verbose_name)

        return super().get_virtual_fields(virtual)
