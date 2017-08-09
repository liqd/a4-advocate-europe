from django.views import generic
from rules.contrib.views import PermissionRequiredMixin

from .models import JourneyEntry


class JourneyEntryCreateView(PermissionRequiredMixin, generic.edit.CreateView):
    template_name = ''
    model = JourneyEntry
    fields = ['title', 'category', 'text']
