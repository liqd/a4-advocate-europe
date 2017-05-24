from django.views import generic

from adhocracy4.modules.models import Module


class ModuleMixin(generic.detail.SingleObjectMixin):
    model = Module

    def dispatch(self, request, *args, **kwargs):
        self.module = self.get_object()
        self.object = self.module
        return super().dispatch(request, *args, **kwargs)
