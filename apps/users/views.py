from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.views import generic
from rules.compat import access_mixins as mixins

from adhocracy4.filters import views as filter_views

from apps.ideas import models as idea_models

from . import models as user_models
from . import filters, forms


class ProfileView(filter_views.FilteredListView):
    template_name = 'advocate_europe_users/profile.html'
    paginator_class = Paginator
    filter_set = filters.ProfileIdeaFilterSet
    queryset = idea_models.Idea.objects.annotate_comment_count()\
        .annotate_positive_rating_count()
    action_count = 10

    @property
    def paginate_by(self):
        if self.request.user == self.user:
            return 8
        else:
            return 9

    def filter_kwargs(self):
        kwargs = super().filter_kwargs()
        kwargs['user'] = self.user
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        username = kwargs['username']
        self.user = get_object_or_404(user_models.User, username=username)
        return super().dispatch(request, *args, **kwargs)

    @property
    def actions(self):
        qs = self.user.action_set.all()
        qs = qs.filter_public().exclude_updates()[:self.action_count]
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
