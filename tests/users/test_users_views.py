import pytest

from django.core.urlresolvers import reverse

from faker import Faker


@pytest.mark.django_db
@pytest.mark.parametrize('user__username', ['Üß +-@. ö'])
def test_profile_view(client, user, idea_sketch_factory):
    """
    Check if profile shows by default only ideas created by user.
    """
    idea1 = idea_sketch_factory(creator=user).idea
    idea2 = idea_sketch_factory(collaborators=[user]).idea
    idea3 = idea_sketch_factory().idea

    url = reverse('profile', kwargs={'username': user.username})
    response = client.get(url)

    assert response.status_code == 200
    assert response.context_data['view'].user == user
    assert idea1 in response.context_data['idea_list']
    assert idea2 not in response.context_data['idea_list']
    assert idea3 not in response.context_data['idea_list']


@pytest.mark.django_db
def test_profile_view_collaboration(client, user, idea_sketch_factory):
    """
    Check if profile shows ideas where user collaborated.
    """
    idea1 = idea_sketch_factory(creator=user).idea
    idea2 = idea_sketch_factory(collaborators=[user]).idea
    idea3 = idea_sketch_factory().idea

    url = reverse('profile', kwargs={'username': user.username})
    response = client.get(url + '?participation=collaborator')
    assert response.status_code == 200
    assert idea1 not in response.context_data['idea_list']
    assert idea2 in response.context_data['idea_list']
    assert idea3 not in response.context_data['idea_list']


@pytest.mark.django_db
def test_profile_edit_city(client, user):
    client.login(email=user.email, password='password')
    url = reverse('edit_profile')

    response = client.post(url, {
        'city': 'foobar',
        'username': user.username
    })

    assert response.status_code == 302

    profile_url = reverse('profile', kwargs={'username': user.username})
    profile_response = client.get(profile_url)

    assert profile_response.status_code == 200
    assert profile_response.context['user'] == user
    assert profile_response.context['user'].city == 'foobar'


@pytest.mark.django_db
def test_profile_edit_username(client, user_factory):
    user1 = user_factory()
    user2 = user_factory()

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
    usernmae = fake.name()
    response = client.post(url, {
        'username': username
    })

    assert response.status_code == 302

    profile_url = reverse('profile', kwargs={'username': user.username})
    profile_response = client.get(profile_url)

    assert profile_response.status_code == 200
    assert profile_response.context['user'] == user
    assert profile_response.context['user'].username == username


@pytest.mark.django_db
def test_profile_edit_birthdate(client, user):
    client.login(email=user.email, password='password')
    url = reverse('edit_profile')
    fake = Faker()

    # valid birthday should be find
    bdate = fake.date(pattern='%Y-%m-%d')
    request = {
        'birthdate': bdate,
        'username': user.username
    }
    response = client.post(url, request)

    assert response.status_code == 302, str(request)

    profile_url = reverse('profile', kwargs={'username': user.username})
    profile_response = client.get(profile_url)

    assert profile_response.status_code == 200
    assert profile_response.context['user'] == user
    assert profile_response.context['user'].birthdate == bdate

    # non date birthday must fail
    request = {
        'birthdate': 'foobar',
        'username': user.username
    }
    response = client.post(url, request)

    assert response.status_code == 200
    assert 'birthdate' in response.context_data['form'].errors

    # birthday in future is valid
    bdate = fake.future_date(end_date="+10d", pattern='%Y-%m-%d')
    request = {
        'birthdate': bdate,
        'username': user.username
    }
    response = client.post(url, request)

    assert response.status_code == 302, str(request)

    profile_url = reverse('profile', kwargs={'username': user.username})
    profile_response = client.get(profile_url)

    #TODO refactoring tests
    assert profile_response.status_code == 200
    assert profile_response.context['user'] == user
    assert profile_response.context['user'].birthdate == bdate
