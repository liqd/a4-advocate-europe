import django_filters
from django.utils.translation import ugettext_lazy as _

from adhocracy4.filters.filters import DefaultsFilterSet
from adhocracy4.projects.models import Project
from apps.ideas import models

from . import widgets


class StatusFilterWidget(widgets.DropdownLinkWidget):
    label = _('Status')


class TopicFilterWidget(widgets.DropdownLinkWidget):
    label = _('Topics')

    def __init__(self, attrs=None):
        choices = (('', _('Any')),)
        choices += (models.abstracts.idea_section.
                    IDEA_TOPIC_CHOICES)

        super().__init__(attrs, choices)


class ProjectFilterWidget(widgets.DropdownLinkWidget):
    label = _('Year')


class IdeaFilterSet(DefaultsFilterSet):

    defaults = {}

    idea_topics = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=TopicFilterWidget
    )

    project_year = django_filters.ModelChoiceFilter(
        queryset=Project.objects.order_by('name'),
        widget=ProjectFilterWidget,
    )

    def what_status(self, queryset, name, value):
        if value == 'all':
            qs = queryset.all()
        elif value == 'idea_sketch':
            qs = queryset.filter(proposal__isnull=True)
        elif value == 'proposal':
            qs = queryset.filter(proposal__isnull=False)
        elif value == 'camp':
            qs = queryset.filter(visit_camp=True)
        else:
            qs = queryset.all()
        return qs

    status = django_filters.ChoiceFilter(
        name='idea_subtitle',
        method='what_status',
        choices=(
            ('idea_sketch', _('Idea Sketch')),
            ('community_award', _('Community Award Winner')),
            ('camp', _('Invited to Camp')),
            ('proposal', _('Proposal')),
            ('winner', _('Winner'))
        ),
        widget=StatusFilterWidget
    )

    class Meta:
        model = models.Idea
        fields = ['status', 'idea_topics', 'project_year']
