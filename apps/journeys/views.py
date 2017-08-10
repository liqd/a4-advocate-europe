from django.views import generic

from apps.ideas.models import Idea

from .models import JourneyEntry


class JourneyEntryCreateView(generic.edit.CreateView
                             ):
    # permission_required = 'advocate_europe_ideas.export_idea'
    model = JourneyEntry
    fields = ['title', 'category', 'text']

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

    def dispatch(self, *args, **kwargs):
        idea_slug = self.kwargs[self.slug_url_kwarg]
        self.idea = Idea.objects.get(slug=idea_slug)
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.idea = self.idea
        return super().form_valid(form)
