import pytest

from apps.ideas import filters, models


@pytest.mark.django_db
def test_idea_list_view(idea_sketch_factory, idea_factory, proposal_factory):

    idea1 = idea_factory(visit_camp=False)
    idea2 = idea_factory(visit_camp=False)
    idea3 = idea_factory(visit_camp=True)

    idea_sketch_factory(idea=idea1)
    idea_sketch_factory(idea=idea2)
    proposal_factory(idea=idea3)

    ALL_POSSIBLE_PARAMS = [('idea_sketch', 2),
                           ('community_award', 0),
                           ('camp', 1),
                           ('proposal', 1),
                           ('winner', 0),
                           ('', 3)]

    idea_filter_set = filters.IdeaFilterSet(data={})

    for param, count in ALL_POSSIBLE_PARAMS:
        assert (lambda p: (idea_filter_set.
                           what_status(models.Idea.objects.all(),
                                       'some_name', p)
                           ).count()
                )(param) == count
