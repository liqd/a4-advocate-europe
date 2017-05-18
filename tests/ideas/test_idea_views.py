import pytest
from apps.ideas import views


@pytest.mark.django_db
def test_idea_space(rf, idea_sketch_factory, proposal_factory):
    idea_sketch_factory()
    idea_sketch_factory()
    proposal_factory()

    view = views.IdeaListView.as_view()
    request = rf.get('/idea')
    response = view(request)
    assert len(response.context_data['object_list']) == 3
    assert response.status_code == 200
