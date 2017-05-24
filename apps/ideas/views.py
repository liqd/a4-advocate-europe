import csv
import os

from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.http import Http404, HttpResponse
from django.shortcuts import redirect
from django.utils.http import is_safe_url
from django.utils.translation import ugettext as _
from django.views import generic
from formtools.wizard.views import SessionWizardView
from rules.contrib.views import PermissionRequiredMixin

from apps.invites.models import IdeaSketchInvite
from apps.wizards import mixins as wizard_mixins

from . import forms, mixins
from .models import Idea, IdeaSketch, IdeaSketchArchived, Proposal, abstracts


class IdeaSketchExportView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'advocate_europe_ideas.export_ideasketch'
    model = IdeaSketch

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv; charset=utf-8')
        response['Content-Disposition'] = (
            'attachment; filename="ideasketches.csv"'
        )

        # Selects all parent classes named ideas.models.abstracts.*Section
        abstracts_module_name = abstracts.__name__ + '.'
        abstract_sections = [
            base_model for base_model in self.model.__mro__
            if base_model.__module__.startswith(abstracts_module_name)
            and base_model.__name__.endswith('Section')
            ]

        field_names = ['id']
        for section in abstract_sections:
            for field in section._meta.concrete_fields:
                field_names.append(field.name)

        writer = csv.writer(response)
        writer.writerow(field_names)

        for idea in self.get_queryset():
            data = [str(getattr(idea, name)) for name in field_names]
            writer.writerow(data)

        return response


class IdeaSketchCreateWizard(PermissionRequiredMixin,
                             mixins.ModuleMixin,
                             wizard_mixins.CustomWizardMixin,
                             SessionWizardView):
    permission_required = 'advocate_europe_ideas.add_ideasketch'
    file_storage = FileSystemStorage(
        location=os.path.join(settings.MEDIA_ROOT, 'idea_sketch_images'))
    title = _('create an idea')

    def done(self, form_list, **kwargs):
        special_fields = ['accept_conditions', 'collaborators_emails']

        data = self.get_all_cleaned_data()
        idea_sketch = IdeaSketch.objects.create(
            creator=self.request.user,
            module=self.module,
            **{
                field: value for field, value in data.items()
                if field not in special_fields
                }
        )

        for name, email in data['collaborators_emails']:
            IdeaSketchInvite.objects.invite(
                self.request.user,
                idea_sketch,
                email
            )

        return redirect(idea_sketch.get_absolute_url())

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()


class IdeaSketchEditView(
    PermissionRequiredMixin,
    SuccessMessageMixin,
    generic.UpdateView
):
    permission_required = 'advocate_europe_ideas.add_ideasketch'
    file_storage = FileSystemStorage(
        location=os.path.join(settings.MEDIA_ROOT, 'idea_sketch_images'))
    model = IdeaSketch
    template_name = 'advocate_europe_ideas/ideasketch_update_form.html'
    success_message = _('Ideasketch saved')

    form_classes = [
        forms.ApplicantSectionForm,
        forms.PartnersSectionForm,
        forms.IdeaSectionForm,
        forms.ImpactSectionForm,
        forms.CollaborationCampSectionForm
    ]

    def dispatch(self, request, *args, **kwargs):
        form_number = self.kwargs.get('form_number', '0')
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
        if (next and is_safe_url(next)):
            return next
        else:
            return self.request.path

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()


class IdeaDetailView(generic.DetailView):
    model = Idea

    @property
    def idea_dict(self):
        return model_to_dict(self.object)

    def get_context_data(self, **kwargs):
        idea_list = []
        idea_list.append((_('Idea pitch'), self.object.idea_pitch))
        if self.object.idea_location_specify:
            idea_list.append((_('Where does your idea take place?'),
                              self.object.idea_location_specify))
        idea_list.append((_('Why does Europe need your idea?'),
                          self.object.challenge))
        idea_list.append((_('What is your impact?'), self.object.outcome))
        idea_list.append((_('How do you get there?'), self.object.plan))
        idea_list.append((_('What is your story?'), self.object.importance))
        if self.object.reach_out:
            idea_list.append((_('What do you need from the Advocate Europe '
                                'community?'), self.object.reach_out))

        partner_list = []
        if (self.object.partner_organisation_1_name
                or self.object.partner_organisation_1_website):
            partner_list.append((self.object.partner_organisation_1_name,
                                 self.object.partner_organisation_1_website,
                                 self.object.
                                 get_partner_organisation_1_country_display))
        if (self.object.partner_organisation_2_name
                or self.object.partner_organisation_2_website):
            partner_list.append((self.object.partner_organisation_2_name,
                                 self.object.partner_organisation_2_website,
                                 self.object.
                                 get_partner_organisation_2_country_display))
        if (self.object.partner_organisation_3_name
                or self.object.partner_organisation_3_website):
            partner_list.append((self.object.partner_organisation_3_name,
                                 self.object.partner_organisation_3_website,
                                 self.object.
                                 get_partner_organisation_3_country_display))

        context = super().get_context_data(**kwargs)
        context['idea_list'] = idea_list
        context['partner_list'] = partner_list
        return context


class IdeaMixin(generic.detail.SingleObjectMixin):
    model = Idea

    def dispatch(self, request, *args, **kwargs):
        self.idea = self.get_object()
        self.object = self.idea
        return super().dispatch(request, *args, **kwargs)


class ProposalCreateWizard(PermissionRequiredMixin,
                           SessionWizardView,
                           IdeaMixin):
    permission_required = 'advocate_europe_ideas.add_ideasketch'
    file_storage = FileSystemStorage(
        location=os.path.join(settings.MEDIA_ROOT, 'idea_sketch_images'))
    title = _('create a proposal')

    def get_form_initial(self, step):
        initial = self.initial_dict.get(step, {})
        form = self.form_list[step]
        for field in form.base_fields:
            if hasattr(self.idea, field):
                initial[field] = getattr(self.idea, field)
        return initial

    def done(self, form_list, **kwargs):
        idea_sketch_archive = IdeaSketchArchived(idea=self.idea)
        for field in self.idea._meta.fields:
            setattr(idea_sketch_archive,
                    field.name,
                    getattr(self.idea, field.name))
        idea_sketch_archive.save()

        special_fields = ['accept_conditions', 'collaborators_emails']

        proposal_data = self.get_cleaned_data_for_step('4')
        data = self.get_all_cleaned_data()

        proposal = Proposal(
            idea_ptr=self.idea,
            creator=self.request.user,
            module=self.idea.module,
            **{
                field: value for field, value in proposal_data.items()
                if field not in special_fields
            }
        )
        proposal.save()
        merged_data = self.idea.__dict__.copy()
        merged_data.update(data)
        proposal.__dict__.update(merged_data)
        proposal.save()

        return redirect(proposal.get_absolute_url())


class IdeaListView(generic.ListView):
    queryset = Idea.objects.annotate_comment_count()
    paginator_class = Paginator
    paginate_by = 12
