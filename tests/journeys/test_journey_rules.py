import pytest
import rules

from tests.factories import UserFactory


@pytest.mark.django_db
def test_journey_rules(admin, user, proposal_factory):
    proposal = proposal_factory()
    creator = UserFactory()
    proposal.creator = creator
    collaborator = UserFactory()
    proposal.collaborators = [collaborator]

    # proposal not winner
    assert not rules.has_perm('advocate_europe_ideas.add_journey',
                              user, proposal)
    assert not rules.has_perm('advocate_europe_ideas.add_journey',
                              creator, proposal)
    assert not rules.has_perm('advocate_europe_ideas.add_journey',
                              collaborator, proposal)
    assert rules.has_perm('advocate_europe_ideas.add_journey', admin, proposal)

    # proposal is winner!
    proposal.is_winner = True
    assert not rules.has_perm('advocate_europe_ideas.add_journey',
                              user, proposal)
    assert rules.has_perm('advocate_europe_ideas.add_journey',
                          creator, proposal)
    assert rules.has_perm('advocate_europe_ideas.add_journey',
                          collaborator, proposal)
    assert rules.has_perm('advocate_europe_ideas.add_journey', admin, proposal)
