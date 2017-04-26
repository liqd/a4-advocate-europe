import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect
from django.views import generic
from formtools.wizard.views import SessionWizardView

from adhocracy4.modules.models import Module

from .models import IdeaSketch


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

    def get_context_data(self, **kwargs):
        idea_tab_dict = {}
        idea_tab_dict['Idea pitch'] = self.object.idea_pitch
        idea_tab_dict['Challenge'] = self.object.challenge
        idea_tab_dict['Outcome'] = self.object.outcome
        idea_tab_dict['Plan'] = self.object.plan
        idea_tab_dict['Importance'] = self.object.importance

        context = super().get_context_data(**kwargs)
        context['idea_tab_dict'] = idea_tab_dict
        return context


class IdeaSketchListView(generic.ListView):
    model = IdeaSketch
    paginate_by = 12
