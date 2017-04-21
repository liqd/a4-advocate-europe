import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views import generic
from formtools.wizard.views import SessionWizardView

from adhocracy4.modules.models import Module

from .models import IdeaSketch


class IdeaSketchCreateWizard(SessionWizardView):
    file_storage = FileSystemStorage(
        location=os.path.join(settings.MEDIA_ROOT, 'idea_sketch_images'))

    def done(self, form_list, **kwargs):
        forms = [form.cleaned_data for form in form_list]
        idea_sketch = IdeaSketch()
        idea_sketch.creator = self.request.user

        mod_slug = self.kwargs['slug']
        mod = Module.objects.get(slug=mod_slug)
        idea_sketch.module = mod

        for form in forms:
            for key, value in form.items():
                setattr(idea_sketch, key, value)

        idea_sketch.save()

        return HttpResponseRedirect(
            reverse('idea-sketch-detail', kwargs={'slug': idea_sketch.slug}))


class IdeaSketchDetailView(generic.DetailView):
    model = IdeaSketch
