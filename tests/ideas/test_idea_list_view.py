import pytest

from apps.ideas import views


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
