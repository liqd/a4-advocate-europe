import django_filters
from django.db import models
from django.forms.utils import flatatt
from django.utils.translation import ugettext_lazy as _

from adhocracy4.filters.filters import DefaultsFilterSet

from apps.ideas import models as idea_models


class LinkWidget(django_filters.widgets.LinkWidget):
    default_list_attrs = {'class': 'filter-list'}
    default_item_attrs = {'class': 'filter-list-item'}

    def __init__(self, attrs=None):
        super().__init__(attrs=self.default_list_attrs.copy())

    def option_string(self):
        return (
            '<li {attrs}><a%(attrs)s href="?%(query_string)s">'
            '%(label)s</a></li>'
        ).format(
            attrs=flatatt(self.default_item_attrs)
        )


class LinkSortWidget(LinkWidget):
    default_list_attrs = {'class': 'filter-list filter-list-sort'}


class ProfileIdeaFilterSet(DefaultsFilterSet):

    defaults = {
        'ordering': 'newest',
        'participation': 'creator_or_collaborator',
    }

    class Meta:
        model = idea_models.Idea
        fields = ['participation', 'ordering']

    def __init__(self, user, data, *args, **kwargs):
        data = data.copy()
        self.user = user

        super().__init__(data, *args, **kwargs)

    def participation_filter(self, queryset, name, value):
        if value == 'creator_or_collaborator':
            return queryset.filter(
                models.Q(creator=self.user)
                | models.Q(collaborators=self.user)
            )
        elif value == 'supporter':
            return queryset.filter(
                ratings__creator=self.user,
                ratings__value=1
            )
        elif value == 'watcher':
            return queryset.filter(
                ideafollow__creator=self.user,
                ideafollow__enabled=True,
            )
        else:
            return queryset.filter_by_participant(self.user)

    participation = django_filters.ChoiceFilter(
        method='participation_filter',
        choices=(
            ('creator_or_collaborator', _('Submitted')),
            ('watcher', _('Watching')),
            ('supporter', _('Supporting')),
        ),
        empty_label=None,
        widget=LinkWidget,
    )

    ordering = django_filters.OrderingFilter(
        fields=(
            ('-created', 'newest'),
            ('idea_title', 'alphabetical'),
        ),
        choices=(
            ('newest', _('Newest')),
            ('alphabetical', _('Alphabetical')),
        ),
        empty_label=None,
        widget=LinkSortWidget,
    )
