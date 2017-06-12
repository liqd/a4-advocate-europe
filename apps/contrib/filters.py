import django_filters
from django.utils.translation import ugettext_lazy as _

from adhocracy4.filters.filters import DefaultsFilterSet
from apps.ideas import models

from . import widgets


class OrgaFilterWidget(widgets.DropdownLinkWidget):
    label = _('bli bla blub')


class TopicFilterWidget(widgets.DropdownLinkWidget):
    label = _('idea_topics')

    def __init__(self, attrs=None):
        choices = (('', _('Any')),)
        choices += (models.abstracts.idea_section.
                    IDEA_TOPIC_CHOICES)

        super().__init__(attrs, choices)


class IdeaFilterSet(DefaultsFilterSet):

    defaults = {}

    idea_topics = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=TopicFilterWidget
    )

    organisation_status = django_filters.ChoiceFilter(
        choices=(models.abstracts.applicant_section.
                 ORGANISATION_STATUS_CHOICES),
        widget=OrgaFilterWidget
    )

    class Meta:
        model = models.Idea
        fields = ['idea_topics', 'organisation_status']
