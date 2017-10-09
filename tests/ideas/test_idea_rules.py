import pytest
import rules
from apps.ideas import phases
from tests.factories import UserFactory
from tests.helpers import active_phase


@pytest.mark.django_db
def test_idea_rate_rules(admin, user, idea_sketch_factory, module):
    idea_sketch = idea_sketch_factory(module=module)
    user = UserFactory()
    assert not rules.has_perm('advocate_europe_ideas.rate_idea',
                              user,
                              idea_sketch)
    idea_sketch.creator = user
    assert not rules.has_perm('advocate_europe_ideas.rate_idea',
                              user,
                              idea_sketch)
    idea_sketch.co_workers.add(user)
    assert not rules.has_perm('advocate_europe_ideas.rate_idea',
                              user,
                              idea_sketch)

    user2 = UserFactory()
    idea_sketch2 = idea_sketch_factory(creator=user2, module=module)

    with active_phase(module, phases.CommunityAwardRatingPhase):
        assert not rules.has_perm('advocate_europe_ideas.rate_idea',
                                  user,
                                  idea_sketch)
        assert not rules.has_perm('advocate_europe_ideas.rate_idea',
                                  user,
                                  idea_sketch2)

    @pytest.mark.django_db
    def test_journey_rules(admin, user, proposal_factory):
        proposal = proposal_factory()
        creator = UserFactory()
        proposal.creator = creator
        co_worker = UserFactory()
        proposal.co_workers = [co_worker]

        # proposal not winner
        assert not rules.has_perm('advocate_europe_ideas.add_journey',
                                  user, proposal)
        assert not rules.has_perm('advocate_europe_ideas.add_journey',
                                  creator, proposal)
        assert not rules.has_perm('advocate_europe_ideas.add_journey',
                                  co_worker, proposal)
        assert rules.has_perm('advocate_europe_ideas.add_journey',
                              admin, proposal)

        # proposal is winner!
        proposal.is_winner = True
        assert not rules.has_perm('advocate_europe_ideas.add_journey',
                                  user, proposal)
        assert rules.has_perm('advocate_europe_ideas.add_journey',
                              creator, proposal)
        assert rules.has_perm('advocate_europe_ideas.add_journey',
                              co_worker, proposal)
        assert rules.has_perm('advocate_europe_ideas.add_journey',
                              admin, proposal)
