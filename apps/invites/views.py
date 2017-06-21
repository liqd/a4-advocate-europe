from django.shortcuts import redirect
from django.views import generic
from rules.compat import access_mixins as mixins

from . import forms, models


class InviteDetailView(generic.DetailView):
    model = models.IdeaInvite
    slug_field = 'token'
    slug_url_kwarg = 'invite_token'

    def dispatch(self, request, invite_token, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(
                '{}-update'.format(self.model.__name__.lower()),
                invite_token=invite_token
            )
        else:
            return super().dispatch(request, *args, **kwargs)


class InviteUpdateView(mixins.LoginRequiredMixin,
                       generic.detail.SingleObjectMixin,
                       generic.detail.SingleObjectTemplateResponseMixin,
                       generic.edit.FormMixin,
                       generic.edit.ProcessFormView):
    model = models.IdeaInvite
    form_class = forms.InviteForm
    slug_field = 'token'
    slug_url_kwarg = 'invite_token'
    template_name_suffix = '_form'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        if form.is_accepted():
            self.object.accept(self.request.user)
            return redirect(self.object.subject.get_absolute_url())
        else:
            self.instance.reject()
            return redirect('/')
