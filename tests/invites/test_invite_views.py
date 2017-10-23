import pytest
from django.core.urlresolvers import reverse

from adhocracy4.test.helpers import redirect_target, templates_used


@pytest.mark.django_db
def test_invite_non_loggedin_user(client, invite):
    """
    Without login the detail view should be displayed, prompting to login.
    """

    url = invite.get_absolute_url()
    response = client.get(url)
    detail_template = 'advocate_europe_invites/invite_detail.html'
    assert response.status_code == 200
    assert detail_template in templates_used(response)


@pytest.mark.django_db
def test_invite_loggedin_user(client, user, invite):
    url = invite.get_absolute_url()
    client.force_login(user)
    response = client.get(url)
    assert redirect_target(response) == 'ideainvite-update'

    url = reverse('ideainvite-update', args=[invite.token])
    response = client.get(url)
    form_template = 'advocate_europe_invites/invite_form.html'
    assert form_template in templates_used(response)


@pytest.mark.django_db
def test_invite_reject(client, user, invite):
    url = reverse('ideainvite-update', args=[invite.token])
    client.force_login(user)
    response = client.post(url, {'reject': True})

    assert redirect_target(response) == 'wagtail_serve'
    assert user not in invite.subject.co_workers.all()


@pytest.mark.django_db
def test_invite_accept(client, user, invite):
    url = reverse('ideainvite-update', args=[invite.token])
    client.force_login(user)
    response = client.post(url, {'accept': True})

    assert redirect_target(response) == 'idea-detail'
    assert user in invite.subject.co_workers.all()
