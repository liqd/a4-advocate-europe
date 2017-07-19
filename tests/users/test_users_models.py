import pytest


@pytest.mark.django_db
def test_fallback_avatar(user):
    avatar_path = '/static/images/avatars/avatar-0{}.svg'.format(user.pk)
    assert user.fallback_avatar == avatar_path


@pytest.mark.django_db
def test_avatar_or_fallback_url(user):
    avatar_path = '/static/images/avatars/avatar-0{}.svg'.format(user.pk)
    assert user.avatar_or_fallback_url() == avatar_path
