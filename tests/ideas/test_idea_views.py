import pytest
from django.urls import reverse

from apps.ideas import models, views


@pytest.mark.django_db
def test_idea_detail_view(rf, idea_sketch_factory, proposal_factory):
    ideasketch = idea_sketch_factory()
    proposal = proposal_factory()

    assert ideasketch.type == models.IdeaSketch._meta.verbose_name.title()
    assert proposal.type == models.Proposal._meta.verbose_name.title()

    view = views.IdeaDetailView.as_view()
    request = rf.get('/ideas/')
    response = view(request, slug=ideasketch.slug)
    assert 'idea_list_1' in response.context_data
    assert (response.context_data['idea_list_1'][0] ==
            ('Idea pitch', ideasketch.idea_pitch))
    assert 'partner_list' in response.context_data


@pytest.mark.django_db
def test_idea_sketch_edit_form_has_request(admin, idea_sketch_factory, client):
    client.login(email=admin.email, password='password')
    idea_sketch = idea_sketch_factory()
    url = reverse('idea-sketch-update-form',
                  kwargs={'slug': idea_sketch.slug, 'form_number': '3'})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_proposal_edit_form_has_request(admin, proposal_factory, client):
    client.login(email=admin.email, password='password')
    proposal = proposal_factory()
    url = reverse('proposal-update-form',
                  kwargs={'slug': proposal.slug, 'form_number': '3'})
    response = client.get(url)
    assert response.status_code == 200
