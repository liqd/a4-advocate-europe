import pytest
from django.core.urlresolvers import reverse

from apps.journeys import models


@pytest.mark.django_db
def test_journey_create_view(client, user, proposal_factory):
    proposal = proposal_factory()
    url = reverse('journey-entry-create', kwargs={'slug': proposal.slug})

    client.login(username=user.email, password='password')
    response = client.get(url)
    assert response.status_code == 403

    proposal.creator = user
    proposal.is_winner = True
    proposal.save()

    response = client.get(url)
    assert response.status_code == 200

    journey_entry = {'title': 'Journey Entry',
                     'category': 'fa',
                     'text': 'some text bla bla'}
    response = client.post(url, journey_entry)
    assert response.status_code == 302
    count = models.JourneyEntry.objects.all().count()
    assert count == 1


@pytest.mark.django_db
def test_journey_update_view(client, journey_entry_factory):
    journey_entry = journey_entry_factory()
    user = journey_entry.creator

    client.login(username=user.email, password='password')
    url = reverse('journey-entry-update', kwargs={'pk': journey_entry.pk})
    response = client.get(url)
    assert response.status_code == 200

    data = {'title': journey_entry.title,
            'category': 'fa',
            'text': 'blablabla'}
    response = client.post(url, data)
    updated_entry = models.JourneyEntry.objects.get(id=journey_entry.pk)
    assert updated_entry.text == 'blablabla'
    assert response.status_code == 302


@pytest.mark.django_db
def test_journey_delete_view(client, journey_entry_factory):
    journey_entry = journey_entry_factory()
    user = journey_entry.creator

    client.login(username=user.email, password='password')
    url = reverse('journey-entry-delete', kwargs={'pk': journey_entry.pk})

    response = client.post(url)
    count = models.JourneyEntry.objects.all().count()
    assert count == 0
    assert response.status_code == 302
