import pytest
from django.core.urlresolvers import reverse
from faker import Faker

from apps.users.forms import UserProfileForm


@pytest.mark.django_db
@pytest.mark.parametrize('user__username', ['Üß +-@. ö'])
def test_profile_view(client, user, idea_sketch_factory):
    """
    Check if profile view shows created and collaborated ideas by default.
    """
    idea1 = idea_sketch_factory(creator=user).idea
    idea2 = idea_sketch_factory(collaborators=[user]).idea
    idea3 = idea_sketch_factory().idea

    url = reverse('profile', kwargs={'username': user.username})
    response = client.get(url)

    assert response.status_code == 200
    assert response.context_data['view'].user == user
    assert idea1 in response.context_data['idea_list']
    assert idea2 in response.context_data['idea_list']
    assert idea3 not in response.context_data['idea_list']


@pytest.mark.django_db
def test_profile_view_filter_watch(client, user, user2,
                                   idea_follow_factory, idea_sketch_factory):
    idea_follow1 = idea_follow_factory(followable__creator=user2, creator=user)
    idea_follow2 = idea_follow_factory(
        followable__creator=user2, creator=user, enabled=False
    )
    idea1 = idea_follow1.followable.idea
    idea2 = idea_sketch_factory(creator=user).idea
    idea3 = idea_follow2.followable.idea

    url = reverse('profile', kwargs={'username': user.username})
    response = client.get(url + '?participation=watcher')
    assert response.status_code == 200
    assert idea1 in response.context_data['idea_list']
    assert idea2 not in response.context_data['idea_list']
    assert idea3 not in response.context_data['idea_list']

    response = client.get(url)
    assert response.status_code == 200
    assert idea1 not in response.context_data['idea_list']


@pytest.mark.django_db
def test_profile_edit(client, user):
    client.login(email=user.email, password='password')
    url = reverse('edit_profile')

    response = client.post(url, {
        'europe': 'foobar',
        'username': user.username
    })

    assert response.status_code == 302

    profile_url = reverse('profile', kwargs={'username': user.username})
    profile_response = client.get(profile_url)

    assert profile_response.status_code == 200
    assert profile_response.context['user'] == user
    assert profile_response.context['user'].europe == 'foobar'


@pytest.mark.django_db
def test_profile_edit_username(client, user_factory):
    user1 = user_factory()
    user2 = user_factory()
    fake = Faker()

    client.login(email=user1.email, password='password')
    url = reverse('edit_profile')

    # username already reserved must fail
    request = {
        'username': user2.username
    }
    response = client.post(url, request)
    assert response.status_code == 200
    assert 'username' in response.context_data['form'].errors

    # new user name must work
    username = fake.name()
    response = client.post(url, {
        'username': username
    })

    assert response.status_code == 302

    profile_url = reverse('profile', kwargs={'username': username})
    profile_response = client.get(profile_url)

    assert profile_response.status_code == 200
    assert profile_response.context['user'] == user1
    assert profile_response.context['user'].username == username

    # no user name must fail
    request = {
        'username': ''
    }
    response = client.post(url, request)
    assert response.status_code == 200
    assert 'username' in response.context_data['form'].errors

    request = {}
    response = client.post(url, request)
    assert response.status_code == 200
    assert 'username' in response.context_data['form'].errors


@pytest.mark.django_db
def test_profile_ignore_optional_fields(client, user):
    client.login(email=user.email, password='password')
    url = reverse('edit_profile')
    fake = Faker()

    request = {
        'username': user.username
    }

    # It should be fine to not submit optional fields.
    for name, field in UserProfileForm.base_fields.items():
        if name not in ('username') and field.required:
            request.update({name: fake.text()})

    response = client.post(url, request)
    assert response.status_code == 302
