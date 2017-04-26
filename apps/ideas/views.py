import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import ListView
from formtools.wizard.views import SessionWizardView
from rules.contrib.views import PermissionRequiredMixin

from adhocracy4.modules.models import Module

from .models import IdeaSketch


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


class IdeaSketchDetailView(generic.DetailView):
    model = IdeaSketch

    @property
    def idea_dict(self):
        return model_to_dict(self.object)
