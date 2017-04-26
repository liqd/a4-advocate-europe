import csv
import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic import ListView
from formtools.wizard.views import SessionWizardView
from rules.contrib.views import PermissionRequiredMixin

from adhocracy4.modules.models import Module

from .models import IdeaSketch
from .models.abstracts.applicant_section import AbstractApplicantSection
from .models.abstracts.collaboration_camp_section import \
    AbstractCollaborationCampSection
from .models.abstracts.community_section import AbstractCommunitySection
from .models.abstracts.idea_section import AbstractIdeaSection
from .models.abstracts.impact_section import AbstractImpactSection
from .models.abstracts.partners_section import AbstractPartnersSection


class IdeaSketchExportView(ListView):
    model = IdeaSketch

    def _get_model_fields(self, model):
        excludes = ['id', 'module', 'module_id', 'creator', 'ideacomplete',
                    'item_ptr', 'item_ptr_id', 'idea_image', 'slug',
                    'visit_camp', 'comments', 'ratings']

        field_list = [field for field in model._meta.get_all_field_names()
                      if field not in excludes]
        return field_list

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; ' \
                                          'filename="ideasketches.csv"'

        # used the sections for ordering the fields,
        # but I am not sure if that is enough
        applicant_fields = self._get_model_fields(AbstractApplicantSection)
        partners_fields = self._get_model_fields(AbstractPartnersSection)
        idea_fields = self._get_model_fields(AbstractIdeaSection)
        impact_fields = self._get_model_fields(AbstractImpactSection)
        collaboration_camp_fields = self._get_model_fields(
            AbstractCollaborationCampSection)
        community_fields = self._get_model_fields(AbstractCommunitySection)

        fields = applicant_fields + partners_fields + \
            idea_fields + impact_fields + \
            collaboration_camp_fields + community_fields

        writer = csv.writer(response)
        writer.writerow(fields)

        for idea in self.get_queryset():
            data = [str(
                getattr(idea, field)).replace('\n', ' ').replace('\r', '')
                    for field in fields]
            writer.writerow(data)

        return response


class IdeaSketchListView(ListView):
    model = IdeaSketch
    paginate_by = 12


class IdeaSketchCreateWizard(PermissionRequiredMixin, SessionWizardView):
    permission_required = 'advocate_europe_ideas.add_ideasketch'
    file_storage = FileSystemStorage(
        location=os.path.join(settings.MEDIA_ROOT, 'idea_sketch_images'))

    def done(self, form_list, **kwargs):
        idea_sketch = IdeaSketch()
        idea_sketch.creator = self.request.user

        mod_slug = self.kwargs['slug']
        mod = Module.objects.get(slug=mod_slug)
        idea_sketch.module = mod

        for key, value in self.get_all_cleaned_data().items():
            setattr(idea_sketch, key, value)

        idea_sketch.save()

        return HttpResponseRedirect(
            reverse('idea-sketch-detail', kwargs={'slug': idea_sketch.slug}))

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()


class IdeaSketchDetailView(generic.DetailView):

    model = IdeaSketch

    @property
    def idea_dict(self):
        return model_to_dict(self.object)
