import pytest

from apps.ideas import filters, models


@pytest.mark.django_db
def test_idea_list_view(idea_sketch_factory, proposal_factory):
    idea_sketch_factory()
    idea_sketch_factory()
    proposal_factory()

    ALL_POSSIBLE_PARAMS = [('idea_sketch', 2),
                           ('community_award', 0),
                           ('shortlist', 1),
                           ('proposal', 1),
                           ('winner', 0),
                           ('', 3)]

    idea_filter_set = filters.IdeaFilterSet(data={}, view=None)

    for param, count in ALL_POSSIBLE_PARAMS:
        assert (lambda p: (idea_filter_set.
                           what_status(models.Idea.objects.all(),
                                       'some_name', p)
                           ).count()
                )(param) == count
