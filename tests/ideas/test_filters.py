import pytest

from apps.ideas import filters, models


@pytest.mark.django_db
def test_idea_list_view(idea_sketch_factory, proposal_factory):
    idea_sketch_factory()
    idea_sketch_factory()
    proposal_factory()

    idea_filter_set = filters.IdeaFilterSet(query_data={})

    filter_idea = (idea_filter_set.
                   what_status(models.Idea.objects.all(),
                               'some_name', 'idea_sketch')
                   )
    assert filter_idea.count() == 2

    filter_idea = (idea_filter_set.
                   what_status(models.Idea.objects.all(),
                               'some_name', 'community_award')
                   )
    assert filter_idea.count() == 0

    filter_idea = (idea_filter_set.
                   what_status(models.Idea.objects.all(),
                               'some_name', 'camp')
                   )
    assert filter_idea.count() == 1

    filter_idea = (idea_filter_set.
                   what_status(models.Idea.objects.all(),
                               'some_name', 'proposal')
                   )
    assert filter_idea.count() == 1

    filter_idea = (idea_filter_set.
                   what_status(models.Idea.objects.all(),
                               'some_name', 'winner')
                   )
    assert filter_idea.count() == 0

    filter_idea = (idea_filter_set.
                   what_status(models.Idea.objects.all(),
                               'some_name', '')
                   )
    assert filter_idea.count() == 3
