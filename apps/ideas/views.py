import csv
import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.forms.models import model_to_dict
from django.utils.translation import ugettext as _
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import generic
from formtools.wizard.views import SessionWizardView
from rules.contrib.views import PermissionRequiredMixin

from adhocracy4.modules.models import Module

from apps.invites.models import IdeaSketchInvite
from .models import IdeaSketch, abstracts


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


class ModuleMixin(generic.detail.SingleObjectMixin):
    model = Module

    def dispatch(self, request, *args, **kwargs):
        self.module = self.get_object()
        self.object = self.module
        return super().dispatch(request, *args, **kwargs)


class IdeaSketchCreateWizard(PermissionRequiredMixin,
                             ModuleMixin,
                             SessionWizardView):
    permission_required = 'advocate_europe_ideas.add_ideasketch'
    file_storage = FileSystemStorage(
        location=os.path.join(settings.MEDIA_ROOT, 'idea_sketch_images'))

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


class IdeaSketchDetailView(generic.DetailView):

    model = IdeaSketch

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
                                 self.object.partner_organisation_1_country))
        if (self.object.partner_organisation_2_name
                or self.object.partner_organisation_2_website):
            partner_list.append((self.object.partner_organisation_2_name,
                                 self.object.partner_organisation_2_website,
                                 self.object.partner_organisation_2_country))
        if (self.object.partner_organisation_3_name
                or self.object.partner_organisation_3_website):
            partner_list.append((self.object.partner_organisation_3_name,
                                 self.object.partner_organisation_3_website,
                                 self.object.partner_organisation_3_country))

        context = super().get_context_data(**kwargs)
        context['idea_list'] = idea_list
        context['partner_list'] = partner_list
        return context


class IdeaSketchListView(generic.ListView):
    model = IdeaSketch
    paginate_by = 12
