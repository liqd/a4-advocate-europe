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

from adhocracy4.modules.models import Module

from .models import IdeaSketch, abstracts


class IdeaSketchExportView(ListView):
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


class IdeaSketchListView(ListView):
    model = IdeaSketch
    paginate_by = 12


class IdeaSketchCreateWizard(SessionWizardView):
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


class IdeaSketchDetailView(generic.DetailView):
    model = IdeaSketch

    @property
    def idea_dict(self):
        return model_to_dict(self.object)
