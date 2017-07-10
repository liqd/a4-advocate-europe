from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.views import generic

from apps.ideas import models as idea_models
from apps.actions import views as action_view

from . import filters, models


class KwargsFilteredListView(generic.ListView):
    """
    Needs to be moved to adhocracy4.
    """

    def filter_kwargs(self):
        default_kwargs = {
            'data': self.request.GET,
            'request': self.request,
            'queryset': super().get_queryset(),
        }

        return default_kwargs

    def filter(self):
        return self.filter_set(
            **self.filter_kwargs()
        )

    def get_queryset(self):
        qs = self.filter().qs
        return qs


class ProfileView(action_view.ActivityView, KwargsFilteredListView):
    template_name = 'advocate_europe_users/profile.html'
    paginator_class = Paginator
    paginate_by = 9
    filter_set = filters.ProfileIdeaFilterSet
    queryset = idea_models.Idea.objects.annotate_comment_count()

    def filter_kwargs(self):
        kwargs = super().filter_kwargs()
        kwargs['user'] = self.user
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        username = kwargs['username']
        self.user = get_object_or_404(models.User, username=username)
        return super().dispatch(request, *args, **kwargs)
