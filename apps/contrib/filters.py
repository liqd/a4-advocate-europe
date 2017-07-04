import django_filters
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from adhocracy4.filters.filters import DefaultsFilterSet
from adhocracy4.projects.models import Project
from apps.ideas import models


from . import widgets


class StatusFilterWidget(widgets.DropdownLinkWidget):
    label = _('Phase')


class TopicFilterWidget(widgets.DropdownLinkWidget):
    label = _('Topic')

    def __init__(self, attrs=None):
        choices = (('', _('All')),)
        choices += (models.abstracts.idea_section.
                    IDEA_TOPIC_CHOICES)

        super().__init__(attrs, choices)


class ProjectFilterWidget(widgets.DropdownLinkWidget):
    label = _('Project')


class OrderingFilterWidget(widgets.DropdownLinkWidget):
    label = _('Sorting')
    right = True


class FreetextFilterWidget(widgets.TextInputWidget):
    label = _('Search')


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
            ('comments', _('Comments')),
            ('title', _('Idea Title')),
        ),
        empty_label=None,
        widget=OrderingFilterWidget
    )

    def search_multi_fields(self, queryset, name, value):
        qs = queryset.filter(Q(idea_pitch__icontains=value) |
                             Q(idea_title__icontains=value) |
                             Q(idea_subtitle__icontains=value)
                             )
        return qs

    search = django_filters.CharFilter(
        method='search_multi_fields',
        widget=FreetextFilterWidget,
    )

    class Meta:
        model = models.Idea
        fields = ['search', 'project', 'status', 'idea_topics', 'ordering']
