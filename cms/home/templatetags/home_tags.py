from django import template
from django.core import exceptions

from adhocracy4.projects.models import Project
from apps.ideas.filters import IdeaFilterSet
from apps.ideas.models import Idea

register = template.Library()


@register.assignment_tag(takes_context=False)
def load_ideas(year, topic, ordering, status):

    ideas = Idea.objects.all().annotate_comment_count()
    idea_filter_set = IdeaFilterSet(data={})

    if year:
        try:
            id = int(year)
            project = Project.objects.get(pk=id)
            ideas = idea_filter_set.filters['project'].filter(ideas, project)
        except (ValueError, exceptions.ObjectDoesNotExist):
            pass
    if topic:
        ideas = idea_filter_set.filters['idea_topics'].filter(ideas, topic)
    if ordering:
        ideas = idea_filter_set.filters['ordering'].filter(ideas, [ordering])
    if status:
        ideas = idea_filter_set.filters['status'].filter(ideas, status)

    return ideas[:20]
