from apps.ideas.forms import BaseForm

from .models import JourneyEntry


class JourneyEntryForm(BaseForm):
    class Meta:
        model = JourneyEntry
        fields = ['title', 'category', 'text']
