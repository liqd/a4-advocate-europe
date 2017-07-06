import django_filters
from django.utils.translation import ugettext_lazy as _

from adhocracy4.filters.filters import DefaultsFilterSet
from adhocracy4.projects.models import Project
from apps.contrib import widgets

from . import models


class StatusFilterWidget(widgets.DropdownLinkWidget):
    label = _('Status')


class TopicFilterWidget(widgets.DropdownLinkWidget):
    label = _('Topic')

    def __init__(self, attrs=None):
        choices = (('', _('All')),)
        choices += (models.abstracts.idea_section.
                    IDEA_TOPIC_CHOICES)

        super().__init__(attrs, choices)


class ProjectFilterWidget(widgets.DropdownLinkWidget):
    label = _('Year')


class OrderingFilterWidget(widgets.DropdownLinkWidget):
    label = _('Sorting')
    right = True


class IdeaFilterSet(DefaultsFilterSet):

    defaults = {
        'ordering': 'newest'
    }

    idea_topics = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=TopicFilterWidget,
    )

    project = django_filters.ModelChoiceFilter(
        name='module__project__name',
        queryset=Project.objects.all(),
        widget=ProjectFilterWidget,
    )

    def what_status(self, queryset, name, value):
        if value == 'idea_sketch':
            qs = queryset.filter(proposal__isnull=True)
        elif value == 'proposal':
            qs = queryset.filter(proposal__isnull=False)
        elif value == 'community_award':
            qs = queryset.filter(community_award_winner=True)
        elif value == 'camp':
            qs = queryset.filter(visit_camp=True)
        elif value == 'winner':
            qs = queryset.filter(is_winner=True)
        else:
            qs = queryset.all()
        return qs

    status = django_filters.ChoiceFilter(
        method='what_status',
        choices=(
            ('idea_sketch', _('Idea Sketch')),
            ('community_award', _('Community Award Winner')),
            ('camp', _('Invited to Collaboration Camp')),
            ('proposal', _('Proposal')),
            ('winner', _('Winner'))
        ),
        widget=StatusFilterWidget
    )

    ordering = django_filters.OrderingFilter(
        fields=(
            ('-created', 'newest'),
            ('-comment_count', 'comments'),
            ('idea_title', 'title'),
        ),
        choices=(
            ('newest', _('Most Recent')),
            ('comments', _('Most Comments')),
            ('title', _('Alphabetical')),
        ),
        empty_label=None,
        widget=OrderingFilterWidget
    )

    class Meta:
        model = models.Idea
        fields = ['project', 'status', 'idea_topics', 'ordering']
