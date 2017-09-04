import csv
import os

from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.translation import ugettext as _
from django.views import generic
from formtools.wizard.views import SessionWizardView
from rules.contrib.views import PermissionRequiredMixin

from adhocracy4.filters import views as filter_views
from adhocracy4.phases.models import Phase

from apps.wizards import mixins as wizard_mixins

from . import filters, forms, mixins
from .models import Idea, IdeaSketch, IdeaSketchArchived, Proposal


class IdeaExportView(PermissionRequiredMixin, filter_views.FilteredListView):
    permission_required = 'advocate_europe_ideas.export_idea'
    model = Idea
    raise_exception = True
    filter_set = filters.IdeaFilterSet

    def get_queryset(self):
        queryset = super().get_queryset().annotate_comment_count()
        return queryset

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv; charset=utf-8')
        response['Content-Disposition'] = (
            'attachment; filename="ideas.csv"'
        )

        exclude_fields = ['module', 'item_ptr', 'members',
                          'slug', 'idea_ptr', 'idea_image',
                          'idea_sketch_archived']

        field_names = []
        for field in IdeaSketch._meta.concrete_fields:
            if (field.name not in exclude_fields and
                    field.name not in field_names):
                field_names.append(field.name)

        for field in Proposal._meta.concrete_fields:
            if (field.name not in exclude_fields and
                    field.name not in field_names):
                field_names.append(field.name)

        field_names.append('link')
        field_names.append('type')

        writer = csv.writer(response, lineterminator='\n',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(field_names)

        del field_names[-2:]

        for idea_base in self.get_queryset():
            has_proposal = hasattr(idea_base, 'proposal')
            idea = idea_base.proposal if has_proposal else idea_base.ideasketch
            data = []
            for name in field_names:
                if hasattr(idea, name):
                    value = getattr(idea, name)
                    if type(value) is list:
                        data.append(str(', '.join(value)))
                    else:
                        data.append(str(value)
                                    .replace('\r', '')
                                    .replace('\n', ''))
                else:
                    data.append('')
            data.append(request.build_absolute_uri(idea.get_absolute_url()))
            data.append(idea.type)
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
    finish_section_text = _('You can add data or edit your idea later.')
    finish_section_btn = _('Submit your idea!')

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
            idea_sketch.ideainvite_set.invite(
                self.request.user,
                email
            )

        return redirect(idea_sketch.get_absolute_url())

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()


class IdeaSketchEditView(
    PermissionRequiredMixin,
    mixins.MultiFormEditMixin,
    SuccessMessageMixin,
    generic.UpdateView
):
    permission_required = 'advocate_europe_ideas.change_idea'
    model = IdeaSketch
    template_name = 'advocate_europe_ideas/idea_update_form.html'
    success_message = _('Ideasketch saved')
    next_view = 'idea-sketch-update-form'

    form_classes = [
        forms.ApplicantSectionForm,
        forms.PartnersSectionForm,
        forms.IdeaSectionForm,
        forms.ImpactSectionForm,
        forms.CollaborationCampSectionForm,
        forms.CommunitySectionEditForm,
    ]

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()


class IdeaDetailView(generic.DetailView):
    display_type = 'idea'
    model = Idea

    @property
    def idea_dict(self):
        return model_to_dict(self.object)

    def get_context_data(self, **kwargs):
        idea_list = []
        proposal_list = []
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

        if hasattr(self.object, 'proposal') and self.object.proposal:
            proposal_list.append((_('Major expenses'),
                                  self.object.proposal.major_expenses))
            proposal_list.append((_('What makes your idea stand apart?'),
                                  self.object.proposal.selection_apart))

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
        context['proposal_list'] = proposal_list
        context['partner_list'] = partner_list
        return context


class IdeaSketchArchivedDetailView(IdeaDetailView):
    display_type = 'idea_sketch_archive'
    model = IdeaSketchArchived
    template_name = 'advocate_europe_ideas/idea_detail.html'
    context_object_name = 'idea'
    slug_field = 'idea__slug'


class ProposalCreateWizard(PermissionRequiredMixin,
                           mixins.IdeaMixin,
                           wizard_mixins.CustomWizardMixin,
                           SessionWizardView,
                           ):
    permission_required = 'advocate_europe_ideas.add_proposal'
    file_storage = FileSystemStorage(
        location=os.path.join(settings.MEDIA_ROOT, 'idea_sketch_images'))
    title = _('create a proposal')
    finish_section_text = _('You can add data or edit your proposal later.')
    finish_section_btn = _('Submit your proposal!')

    def get_form_initial(self, step):
        initial = self.initial_dict.get(step, {})
        form = self.form_list[step]
        for field in form.base_fields:
            if hasattr(self.idea, field):
                initial[field] = getattr(self.idea, field)
        return initial

    def done(self, form_list, **kwargs):
        archive = IdeaSketchArchived(id=self.idea.id)
        for field in archive._meta.get_fields():
            value = getattr(self.idea.ideasketch, field.name)

            if not (field.many_to_many or field.one_to_many):
                setattr(archive, field.name, value)
        archive.save()

        for field in archive._meta.get_fields():
            value = getattr(self.idea.ideasketch, field.name)
            if field.many_to_many or field.one_to_many:
                value = value.all()
                setattr(archive, field.name, value)

        archive.save()

        special_fields = ['accept_conditions', 'collaborators_emails']
        data = self.get_all_cleaned_data()
        proposal = Proposal(
            idea_ptr=self.idea,
            creator=self.request.user,
            module=self.idea.module,
            **{
                field: value for field, value in data.items()
                if field not in special_fields
            }
        )
        proposal.save()
        return redirect(proposal.get_absolute_url())


class ProposalEditView(
    PermissionRequiredMixin,
    mixins.MultiFormEditMixin,
    SuccessMessageMixin,
    generic.UpdateView
):
    permission_required = 'advocate_europe_ideas.change_idea'
    model = Proposal
    template_name = 'advocate_europe_ideas/idea_update_form.html'
    success_message = _('Proposal saved')
    next_view = 'proposal-update-form'

    form_classes = [
        forms.ApplicantSectionForm,
        forms.PartnersSectionForm,
        forms.IdeaSectionForm,
        forms.ImpactSectionForm,
        forms.SelectionCriteriaSectionForm,
        forms.FinanceAndDurationSectionForm,
        forms.CommunitySectionEditForm,
    ]

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()


class IdeaListView(filter_views.FilteredListView):
    model = Idea
    paginator_class = Paginator
    paginate_by = 12
    filter_set = filters.IdeaFilterSet

    @property
    def active_phase(self):
        return Phase.objects.active_phases().last()

    def get_queryset(self):
        queryset = super().get_queryset().annotate_comment_count()
        return queryset

    def filter_kwargs(self):
        default_kwargs = super().filter_kwargs()
        if self.active_phase:
            data = (self.active_phase.content().get_phase_filters(
                self.active_phase.module.project.pk).copy()
            )
            for key in default_kwargs['data']:
                data.setlist(key, [default_kwargs['data'][key]])
            default_kwargs['data'] = data
        return default_kwargs
