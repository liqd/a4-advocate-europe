import pytest
from django.core.urlresolvers import reverse

from apps.ideas.phases import InterimShortlistPublicationPhase

from tests.helpers import active_phase, intercept_emails


@pytest.mark.django_db
def test_extra_object_tools(client, admin, module):
    client.force_login(admin)
    changelist_url = reverse('admin:advocate_europe_ideas_idea_changelist')

    response = client.get(changelist_url)
    object_tools = response.context_data['cl']\
                           .model_admin\
                           .extra_list_object_tools
    assert len(object_tools) == 0

    with active_phase(module, InterimShortlistPublicationPhase):
        response = client.get(changelist_url)
        object_tools = response.context_data['cl']\
                               .model_admin\
                               .extra_list_object_tools
        assert len(object_tools) == 2


@pytest.mark.django_db
def test_notify_shortlist(
        client, admin, module, idea_sketch_factory, idea_follow_factory
):
    """
    Send notifications to shortlist
    """

    idea_sketch_factory(module=module)
    i1 = idea_sketch_factory(module=module, is_on_shortlist=True)
    i2 = idea_sketch_factory(
        module=module,
        is_on_shortlist=True,
        community_award_winner=True
    )
    follow = idea_follow_factory(followable=i1.idea)
    client.force_login(admin)

    # notify shortlist followers
    notifyshortlist_url = reverse(
        'admin:advocate_europe_ideas_idea_notify_shortlist'
    )
    with active_phase(module, InterimShortlistPublicationPhase):
        response = client.get(notifyshortlist_url)
        assert response.status_code == 200
        assert set(response.context_data['ideas']) == set([i1.idea, i2.idea])

        with intercept_emails() as emails:
            data = {'idea_ids': [i1.id, i2.id]}
            response = client.post(notifyshortlist_url, data)

            assert len(emails) == 2

            email0 = emails[0]
            followers = set(
                i2.co_workers.all()
            )
            assert set(email0.get_receivers()) == followers

            email1 = emails[1]
            followers = set(
                i1.co_workers.all()
            )
            followers.add(follow.creator)
            assert set(email1.get_receivers()) == followers


@pytest.mark.django_db
def test_notify_winners(
        client, admin, module, proposal_factory, idea_follow_factory
):
    """
    Send notifications to all winners.

    List the currently selected winners. Send notifications to to winners
    listed even if there has been added an other winner in between.
    """

    p1 = proposal_factory(module=module, is_on_shortlist=True, is_winner=True)
    p2 = proposal_factory(module=module, is_on_shortlist=True)
    proposal_factory(
        module=module,
        is_on_shortlist=True,
        community_award_winner=True
    )
    proposal_factory(module=module)
    follow = idea_follow_factory(followable=p1.idea)
    client.force_login(admin)

    # notify winner followers
    notifywinners_url = reverse(
        'admin:advocate_europe_ideas_idea_notify_winners'
    )

    with active_phase(module, InterimShortlistPublicationPhase):
        response = client.get(notifywinners_url)
        assert response.status_code == 200
        assert list(response.context_data['ideas']) == [p1.idea]

        with intercept_emails() as emails:
            data = {'idea_ids': [p1.id]}
            response = client.post(notifywinners_url, data)

            p2.is_winner = True
            p2.save()

            assert len(emails) == 1
            followers = set(
                p1.co_workers.all()
            )
            followers.add(follow.creator)
            assert set(emails[0].get_receivers()) == followers
