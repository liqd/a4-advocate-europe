import pytest
from django.core.urlresolvers import reverse
from rest_framework import status


@pytest.mark.django_db
def test_anonymous_can_read_follow(apiclient, idea_sketch_factory, user):
    idea = idea_sketch_factory(creator=user, co_workers=[])
    url = reverse('follows-detail', args=[idea.pk])
    response = apiclient.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {'follows': 0}


@pytest.mark.django_db
def test_anonymous_update(apiclient, idea_sketch):
    url = reverse('follows-detail', args=[idea_sketch.pk])
    response = apiclient.put(url, {'enable': True}, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_read_follow_state(apiclient, user2, idea_sketch_factory):
    idea = idea_sketch_factory(co_workers=[])
    url = reverse('follows-detail', args=[idea.pk])
    response = apiclient.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {'follows': 0}

    apiclient.force_authenticate(user=user2)
    response = apiclient.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {'follows': 0, 'enabled': False}


@pytest.mark.django_db
def test_user_create_follow(apiclient, idea_sketch_factory, user2):
    idea_sketch = idea_sketch_factory(co_workers=[])
    url = reverse('follows-detail', args=[idea_sketch.pk])
    apiclient.force_authenticate(user=user2)

    response = apiclient.put(url, {'enabled': True}, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == {'follows': 1, 'enabled': True}

    response = apiclient.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {'follows': 1, 'enabled': True}


@pytest.mark.django_db
def test_user_update_follow(apiclient, idea_follow_factory):
    idea_follow = idea_follow_factory(followable__co_workers=[])
    url = reverse('follows-detail', args=[idea_follow.followable.pk])
    apiclient.force_authenticate(user=idea_follow.creator)

    response = apiclient.put(url, {'enabled': False}, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {'follows': 0, 'enabled': False}

    response = apiclient.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {'follows': 0, 'enabled': False}
