from django.http import Http404
from django.utils.http import is_safe_url
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


class MultiFormEditMixin():
    """
    Allows to edit a large model in smaller parts.

    There should be two routes for this view, one with an aditional form_number
    parameter and one without. For each provided form a (sub)-view is created,
    the user can navigate between the views by submitting them and setting the
    next parameter. It is required that each form can be validated/stored
    independently from the others.
    """
    form_classes = ()
    form_number_keyword = 'form_number'

    def dispatch(self, request, *args, **kwargs):
        form_number = self.kwargs.get(self.form_number_keyword, '0')
        if not form_number.isdecimal():
            raise Http404

        form_number = int(form_number)
        self.form_number = form_number
        if form_number < 0 or len(self.form_classes) <= form_number:
            raise Http404

        self.form_class = self.form_classes[form_number]
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        next = self.request.POST.get('next')
        if (next and is_safe_url(next)):
            return next
        else:
            return self.request.path
