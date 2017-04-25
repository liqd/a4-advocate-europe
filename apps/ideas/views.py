from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import ListView

from .models import IdeaSketch


class IdeaSketchListView(ListView):
    model = IdeaSketch
    paginate_by = 12

    def get_context_data(self, **kwargs):
        ideasketch_list = IdeaSketch.objects.all()

        paginator = Paginator(ideasketch_list, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            ideasketch_list = paginator.page(page)
        except PageNotAnInteger:
            ideasketch_list = paginator.page(1)
        except EmptyPage:
            ideasketch_list = paginator.page(paginator.num_pages)

        # Only show five page numbers in pagination
        index = ideasketch_list.number - 1
        max_index = len(paginator.page_range)
        if index <= 1:
            start_index = 0
            end_index = 4
        elif index >= max_index - 2:
            start_index = max_index - 5 if max_index > 5 else 0
            end_index = max_index
        else:
            start_index = index - 2
            end_index = index + 2
        page_range = paginator.page_range[start_index:end_index+1]

        context = super(IdeaSketchListView, self).get_context_data(**kwargs)
        context['ideasketch_list'] = ideasketch_list
        context['page_range'] = page_range
        return context
