import django_filters
from django.http import QueryDict
from django.utils.translation import ugettext_lazy as _

from apps.ideas import models

from . import widgets


class TopicFilterWidget(widgets.DropdownLinkWidget):
    label = _('organisation_status')

    def __init__(self, attrs=None):
        choices = (models.abstracts.applicant_section.
                   ORGANISATION_STATUS_CHOICES)

        super().__init__(attrs, choices)


class DefaultsFilterSet(django_filters.FilterSet):

    def __init__(self, query_data, *args, **kwargs):
        data = QueryDict(mutable=True)
        data.update(self.defaults)
        data.update(query_data)
        super().__init__(data, *args, **kwargs)


class TopicFilter(DefaultsFilterSet):

    defaults = {
        # 'idea_topics': 'environment'
        'organisation_status': 'non_profit'
    }

    topic = django_filters.ChoiceFilter(
                    name='organisation_status',
                    widget=TopicFilterWidget
                )

    class Meta:
        model = models.Idea
        # fields = ['idea_topics']
        fields = ['organisation_status']
