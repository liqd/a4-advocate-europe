from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.views import generic

from apps.ideas import models as idea_models

from . import models


class ProfileView(generic.ListView):
    model = idea_models.Idea
    template_name = 'advocate_europe_users/profile.html'
    paginator_class = Paginator
    paginate_by = 9

    def dispatch(self, request, *args, **kwargs):
        username = kwargs['username']
        self.user = get_object_or_404(models.User, username=username)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().filter_by_participant(self.user)
