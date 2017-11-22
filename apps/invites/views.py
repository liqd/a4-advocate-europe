from django.http.response import Http404
from django.shortcuts import redirect, render
from django.views import generic
from rules.compat import access_mixins as mixins

from . import forms, models


class InviteDetailView(generic.DetailView):
    model = models.IdeaInvite
    slug_field = 'token'
    slug_url_kwarg = 'invite_token'

    @property
    def template_name(self):
        return '{}/invite_detail.html'.format(self.model._meta.app_label)

    def dispatch(self, request, invite_token, *args, **kwargs):
        if request.user.is_authenticated():
            try:
                models.IdeaInvite.objects.get(token=invite_token)
                return redirect(
                    '{}-update'.format(self.model.__name__.lower()),
                    invite_token=invite_token
                )
            except models.IdeaInvite.DoesNotExist:
                return render(
                    request,
                    '{}/invite_404.html'.format(self.model._meta.app_label)
                )
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return render(
                request,
                '{}/invite_404.html'.format(self.model._meta.app_label)
            )


class InviteUpdateView(mixins.LoginRequiredMixin,
                       generic.detail.SingleObjectMixin,
                       generic.detail.SingleObjectTemplateResponseMixin,
                       generic.edit.FormMixin,
                       generic.edit.ProcessFormView):
    model = models.IdeaInvite
    form_class = forms.InviteForm
    slug_field = 'token'
    slug_url_kwarg = 'invite_token'

    @property
    def template_name(self):
        return '{}/invite_form.html'.format(self.model._meta.app_label)

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        if form.is_accepted():
            self.object.accept(self.request.user)
            return redirect(self.object.subject.get_absolute_url())
        else:
            self.object.reject()
            return redirect('/')
