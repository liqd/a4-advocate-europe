from django.views import generic

from .models import Action


class ActivityView(generic.ListView):
    count = 5

    @property
    def actions(self):
        return Action.objects \
            .public().exclude_updates()[:self.count]


