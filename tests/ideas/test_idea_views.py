import pytest
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse

from apps.ideas import models, views


@pytest.mark.django_db
def test_idea_list_view(rf, idea_sketch_factory, proposal_factory):
    idea_sketch_factory()
    idea_sketch_factory()
    proposal_factory()

    view = views.IdeaListView.as_view()
    request = rf.get('/ideas')
    response = view(request)
    assert len(response.context_data['object_list']) == 3
    assert response.status_code == 200

    request = rf.get('/ideas/?status=proposal')
    response = view(request)
    assert len(response.context_data['object_list']) == 1
    assert response.status_code == 200

    request = rf.get('/ideas/?idea_topics=environment&ordering=newest')
    response = view(request)
    assert len(response.context_data['object_list']) == 3
    assert response.status_code == 200


@pytest.mark.django_db
def test_idea_detail_view(rf, idea_sketch_factory, proposal_factory):
    ideasketch = idea_sketch_factory()
    proposal = proposal_factory()

    assert ideasketch.type == models.IdeaSketch._meta.verbose_name.title()
    assert proposal.type == models.Proposal._meta.verbose_name.title()

    view = views.IdeaDetailView.as_view()
    request = rf.get('/ideas/')
    response = view(request, slug=ideasketch.slug)
    assert 'idea_list' in response.context_data
    assert (response.context_data['idea_list'][0] ==
            ('Idea pitch', ideasketch.idea_pitch))
    assert 'partner_list' in response.context_data


@pytest.mark.django_db
def test_idea_sketch_export_view_user(rf, user):
    view = views.IdeaExportView.as_view()
    request = rf.get('/ideas/list/export')
    request.user = user
    with pytest.raises(PermissionDenied):
        view(request)


@pytest.mark.django_db
def test_idea_export_view_admin(rf, admin, idea_sketch_factory,
                                proposal_factory):
    idea_sketch_factory()
    idea_sketch_factory()
    proposal_factory()

    view = views.IdeaExportView.as_view()
    request = rf.get('/ideas/list/export')
    request.user = admin
    response = view(request)
    assert response.status_code == 200
    assert (response._headers['content-type'] ==
            ('Content-Type', 'text/csv; charset=utf-8'))
    assert (response._headers['content-disposition'] ==
            ('Content-Disposition', 'attachment; filename="ideas.csv"'))

    content_line = response.content.split(b'\n')
    assert len(content_line) == 5

    assert len(str(content_line[0]).split('","')) == 58
    assert len(str(content_line[1]).split('","')) == 58
    assert len(str(content_line[3]).split('","')) == 58


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
