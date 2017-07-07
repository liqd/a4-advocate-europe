import pytest

from django.core.urlresolvers import reverse


@pytest.mark.django_db
@pytest.mark.parametrize('user__username', ['Üß +-@. ö'])
def test_profile_view(client, user, idea_sketch_factory):
    idea1 = idea_sketch_factory(creator=user).idea
    idea2 = idea_sketch_factory().idea

    url = reverse('profile', kwargs={'username': user.username})
    response = client.get(url)

    assert response.status_code == 200
    assert response.context_data['view'].user == user
    assert idea1 in response.context_data['idea_list']
    assert idea2 not in response.context_data['idea_list']
