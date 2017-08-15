import pytest
from django.core.urlresolvers import reverse

from apps.journeys import models


@pytest.mark.django_db
def test_journey_create_view(client, user, admin, proposal_factory):
    proposal = proposal_factory()
    url = reverse('journey-entry-create', kwargs={'slug': proposal.slug})

    client.login(username=user.email, password='password')
    response = client.get(url)
    assert response.status_code == 403

    client.login(username=admin.email, password='password')
    response = client.get(url)
    assert response.status_code == 200

    journey_entry = {'title': 'Journey Entry',
                     'category': 'fa',
                     'text': 'some text bla bla'}
    response = client.post(url, journey_entry)
    assert response.status_code == 302
    count = models.Idea.objects.all().count()
    assert count == 1


@pytest.mark.django_db
def test_journey_update_view(admin, client, journey_entry_factory):
    journey_entry = journey_entry_factory()
    user = journey_entry.creator

    # import pdb; pdb.set_trace()
    client.login(username=user.email, password='password')
    client.login(username=admin.email, password='password')
    url = reverse('journey-entry-update', kwargs={'pk': journey_entry.pk})
    response = client.get(url)
    assert response.status_code == 200
