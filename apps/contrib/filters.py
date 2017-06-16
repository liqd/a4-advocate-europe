import django_filters
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


def make_project_choices():
    choices = []
    projects = []
    try:
        for project in Project.objects.all():
            projects += [project.name]
    except Project.DoesNotExist:
        pass
    for project in projects:
        choices += (project, project),
    return choices


class OrderingFilterWidget(widgets.DropdownLinkWidget):
    label = _('Sorting')


class IdeaFilterSet(DefaultsFilterSet):

    defaults = {}

    idea_topics = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=TopicFilterWidget,
    )

    def what_project(self, queryset, name, value):
        qs = queryset.filter(module__project__name=value)
        return qs

    project = django_filters.ChoiceFilter(
        method='what_project',
        choices=make_project_choices(),
        widget=ProjectFilterWidget,
    )

    def what_status(self, queryset, name, value):
        if value == 'idea_sketch':
            qs = queryset.filter(is_proposal=False)
        elif value == 'proposal':
            qs = queryset.filter(is_proposal=True)
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

    def order(self, queryset, name, value):
        qs = queryset.annotate_comment_count()
        if value[0] == 'comment_count':
            qs = qs.order_by('-comment_count')
        else:
            qs = qs.order_by(value[0])
        return qs

    ordering = django_filters.OrderingFilter(
        method='order',
        fields=(
            ('created', 'created'),
            ('comment_count', 'comment_count'),
            ('idea_title', 'idea_title'),
        ),
        choices=(
            ('created', _('Newest')),
            ('comment_count', _('Comments')),
            ('idea_title', _('Idea Title')),
        ),
        widget=OrderingFilterWidget
    )

    # ordering = django_filters.OrderingFilter(
    #     fields=(
    #         ('-created', 'newest'),
    #         ('comment_count', 'comments'),
    #         ('idea_title', 'title'),
    #     ),
    #     choices=(
    #         ('newest', _('Newest')),
    #         ('comments', _('Comments')),
    #         ('title', _('Idea Title')),
    #     ),
    #     widget=OrderingFilterWidget
    # )

    class Meta:
        model = models.Idea
        fields = ['project', 'status', 'idea_topics', 'ordering']
