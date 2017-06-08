import django_filters
from django.http import QueryDict
from django.utils.translation import ugettext_lazy as _

from apps.ideas import models

from . import widgets


class TopicFilterWidget(widgets.DropdownLinkWidget):
    label = _('topic')

    def __init__(self, attrs=None):
        choices = (
            ('all', _('all'))
            ('democracy_participation', _('Democracy and participation')),
            ('arts_cultural_activities',
                _('Arts and (inter-)cultural activities')),
            ('environment', _('Environment')),
            ('social_inclusion', _('Social inclusion')),
            ('migration', _('Migration')),
            ('communities', _('Communities')),
            ('urban_development', _('Urban development')),
            ('education', _('Education'))
        )
        super().__init__(attrs, choices)


class DefaultsFilterSet(django_filters.FilterSet):

    def __init__(self, query_data, *args, **kwargs):
        data = QueryDict(mutable=True)
        data.update(self.defaults)
        data.update(query_data)
        super().__init__(data, *args, **kwargs)


class TopicFilter(DefaultsFilterSet):

    defaults = {
        'idea_topics': 'environment'
    }

    topic = django_filters.ChoiceFilter(
                    name='topics',
                    widget=TopicFilterWidget
                )

    class Meta:
        model = models.Idea
        fields = ['idea_topics']
