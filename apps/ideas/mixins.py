from django.views import generic

from adhocracy4.modules.models import Module

from .models import Idea


class IdeaMixin(generic.detail.SingleObjectMixin):
    model = Idea

    def dispatch(self, request, *args, **kwargs):
        self.idea = self.get_object()
        self.object = self.idea
        return super().dispatch(request, *args, **kwargs)


class ModuleMixin(generic.detail.SingleObjectMixin):
    model = Module

    def dispatch(self, request, *args, **kwargs):
        self.module = self.get_object()
        self.object = self.module
        return super().dispatch(request, *args, **kwargs)
