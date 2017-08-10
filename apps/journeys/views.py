from django.utils.translation import ugettext as _
from django.views import generic

from apps.ideas.models import Idea

from .forms import JourneyEntryForm
from .models import JourneyEntry


class JourneyEntryCreateView(generic.CreateView):
    # permission_required = 'advocate_europe_ideas.export_idea'
    form_class = JourneyEntryForm
    template_name = 'advocate_europe_journeys/journey_entry_form.html'

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


class JourneyEntryUpdateView(generic.UpdateView):
    # permission_required = 'advocate_europe_ideas.export_idea'
    form_class = JourneyEntryForm
    model = JourneyEntry
    template_name = 'advocate_europe_journeys/journey_entry_form.html'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()


class JourneyEntryDeleteView(generic.DeleteView):
    model = JourneyEntry
    success_message = _("Your Journey entry has been deleted")

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

    # def delete(self, request, *args, **kwargs):
    #     messages.success(self.request, self.success_message)
    #     return super(JourneyEntryDeleteView, self).delete(request,
    #                                                       *args, **kwargs)

    # def get_success_url(self):
    #     return reverse('idea-detail',
    #                    kwargs={'slug': self.object.idea.slug})
