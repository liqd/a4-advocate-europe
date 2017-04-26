from django.views.generic import ListView

from .models import IdeaSketch


class IdeaSketchListView(ListView):
    model = IdeaSketch
    paginate_by = 12
