from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.views import generic
from rules.compat import access_mixins as mixins

from apps.ideas import models as idea_models

from . import models as user_models
from . import forms


class ProfileView(generic.ListView):
    model = idea_models.Idea
    template_name = 'advocate_europe_users/profile.html'
    paginator_class = Paginator
    paginate_by = 9

    def dispatch(self, request, *args, **kwargs):
        username = kwargs['username']
        self.user = get_object_or_404(user_models.User, username=username)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter_by_participant(self.user)
        qs = qs.annotate_comment_count()
        return qs


class EditProfileView(mixins.LoginRequiredMixin,
                      SuccessMessageMixin,
                      generic.UpdateView):
    model = user_models.User
    template_name = "advocate_europe_users/profile_form.html"
    success_message = _('Your profile has been updated')
    form_class = forms.UserProfileForm

    def get_object(self):
        return get_object_or_404(user_models.User, pk=self.request.user.id)

    def get_success_url(self):
        return reverse('edit_profile')

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()
