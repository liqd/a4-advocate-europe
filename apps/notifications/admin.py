from django.conf.urls import url
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from adhocracy4.phases import models as phase_models

from . import emails


class NotifyMixin:
    """Provides object tools and view for notifying winners.

    Will sent an email notification to all followers of ideas that are winners
    or on the short list in the last or current module.
    """

    # Required to have the extra_list_object_tools working
    change_list_template = (
        'admin/advocate_europe_notifications/object_tools_change_list.html'
    )

    @property
    def extra_list_object_tools(self):
        """ Custom extension of change list to add additional object-tools."""

        module = self.latest_module
        if module:
            return [
                (
                    'notify_shortlist',
                    'notify shortlist {}'.format(module.name)
                ),
                (
                    'notify_winners',
                    'notify winners {}'.format(module.name)
                ),
            ]
        return []

    @property
    def latest_module(self):
        phase = phase_models.Phase.objects\
                                 .past_and_active_phases()\
                                 .last()
        if phase:
            return phase.module

    def get_urls(self):
        return [
            url(
                r'^notify/shortlist$',
                self.admin_site.admin_view(self.notify_shortlist),
                name='advocate_europe_ideas_idea_notify_shortlist',
            ),
            url(
                r'^notify/winners$',
                self.admin_site.admin_view(self.notify_winners),
                name='advocate_europe_ideas_idea_notify_winners',
            ),
        ] + super().get_urls()

    def _notify(self, request, *, display_winners=False):
        if not self.has_change_permission(request):
            raise PermissionDenied

        if request.method == 'POST':
            idea_id_strs = request.POST.getlist('idea_ids')
            idea_ids = [int(str_id) for str_id in idea_id_strs]

            for idea in self.model.objects.filter(pk__in=idea_ids):
                if display_winners:
                    emails.NotifyFollowersOnWinner.send(idea)
                elif idea.community_award_winner:
                    emails.NotifyFollowersOnCommunityAward.send(idea)
                else:
                    emails.NotifyFollowersOnShortlist.send(idea)

            messages.add_message(
                request,
                messages.INFO,
                'Sent notifications for {} idea(s).'.format(len(idea_id_strs))
            )

            return redirect(
                '{}:{}_{}_changelist'.format(
                    self.admin_site.name,
                    self.model._meta.app_label,
                    self.model._meta.model_name,
                )
            )
        else:
            current_ideas = self.model.objects.filter(
                module=self.latest_module
            )

            if display_winners:
                filters = {'is_winner': True}
            else:
                filters = {'is_on_shortlist': True}

            context = {
                'opts': self.model._meta,
                'display_winners': display_winners,
                'ideas': current_ideas.filter(**filters)
            }
            context.update(self.admin_site.each_context(request))

            return TemplateResponse(
                request,
                [
                    'admin/{}/notify_followers_confirm.html'.format(
                        self.model._meta.app_label
                    ),
                    'admin/notify_followers_confirm.html',
                ],
                context
            )

    def notify_shortlist(self, request):
        return self._notify(request, display_winners=False)

    def notify_winners(self, request):
        return self._notify(request, display_winners=True)
