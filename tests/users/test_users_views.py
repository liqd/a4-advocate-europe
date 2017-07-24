import pytest

from django.core.urlresolvers import reverse


@pytest.mark.django_db
@pytest.mark.parametrize('user__username', ['Üß +-@. ö'])
def test_profile_view(client, user, idea_sketch_factory, idea_factory):
    """
    Check if profile shows by default only ideas created by user.
    """
    idea1 = idea_factory(creator=user)
    idea2 = idea_factory(collaborators=[user])

    idea_sketch1 = idea_sketch_factory(idea=idea1).idea
    idea_sketch2 = idea_sketch_factory(idea=idea2).idea
    idea_sketch3 = idea_sketch_factory().idea

    url = reverse('profile', kwargs={'username': user.username})
    response = client.get(url)

    assert response.status_code == 200
    assert response.context_data['view'].user == user
    assert idea_sketch1 in response.context_data['idea_list']
    assert idea_sketch2 not in response.context_data['idea_list']
    assert idea_sketch3 not in response.context_data['idea_list']


@pytest.mark.django_db
def test_profile_view_collaboration(client, user,
                                    idea_factory, idea_sketch_factory):
    """
    Check if profile shows ideas where user collaborated.

    """
    idea1 = idea_factory(creator=user)
    idea2 = idea_factory(collaborators=[user])

    idea_sketch1 = idea_sketch_factory(idea=idea1).idea
    idea_sketch2 = idea_sketch_factory(idea=idea2).idea
    idea_sketch3 = idea_sketch_factory().idea

    url = reverse('profile', kwargs={'username': user.username})
    response = client.get(url + '?participation=collaborator')
    assert response.status_code == 200
    assert idea_sketch1 not in response.context_data['idea_list']
    assert idea_sketch2 in response.context_data['idea_list']
    assert idea_sketch3 not in response.context_data['idea_list']
