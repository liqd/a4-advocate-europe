from django.shortcuts import render

from .models import IdeaSketch


def ideasketchlist(request):
    ideasketches = IdeaSketch.objects.all()
    context = {'ideasketches': ideasketches}
    return render(request,
                  'advocate_europe_ideas/idea-sketch-list.html',
                  context
                  )


# class IdeaSketchListView():

#     def get_context(request):
#         ideasketches = IdeaSketch.objects.all()

#         return ideasketches
