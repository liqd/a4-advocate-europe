import pytest

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


@pytest.mark.django_db
def test_idea_detail_view(rf, idea_sketch_factory, proposal_factory):
    ideasketch = idea_sketch_factory()
    proposal = proposal_factory()

    assert ideasketch.type == models.IdeaSketch._meta.verbose_name.title()
    assert proposal.type == models.Proposal._meta.verbose_name.title()

    view = views.IdeaDetailView.as_view()
    request = rf.get('/ideas/{}/'.format(
        ideasketch.slug, {'slug': ideasketch.slug}))
    response = view(request, slug=ideasketch.slug)
    assert 'idea_list' in response.context_data
    assert (response.context_data['idea_list'][0] ==
            ('Idea pitch', ideasketch.idea_pitch))
    assert 'partner_list' in response.context_data
