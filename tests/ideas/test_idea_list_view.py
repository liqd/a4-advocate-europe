import pytest

from apps.ideas import phases, views

from tests.helpers import active_phase


@pytest.mark.django_db
def test_idea_list_view(rf, idea_sketch_factory, proposal_factory):
    idea_sketch_factory()
    idea_sketch_factory()
    proposal_factory()

    view = views.IdeaListView.as_view()
    request = rf.get('/ideas')
    response = view(request)
    # default filter settings for the idea filters are 'status': 'winner'
    assert len(response.context_data['object_list']) == 0
    assert response.status_code == 200

    request = rf.get('/ideas/?status=proposal')
    response = view(request)
    assert len(response.context_data['object_list']) == 1
    assert response.status_code == 200

    request = rf.get('/ideas/?idea_topics=environment&ordering=newest&'
                     'project=&status=')
    response = view(request)
    assert len(response.context_data['object_list']) == 3
    assert response.status_code == 200


@pytest.mark.django_db
def test_idea_list_view_idea_sketch_phase(rf, admin, idea_sketch_factory,
                                          proposal_factory, module):
    # the default filters for the ideaSketchPhase set
    # 'status': 'idea_sketch' and the year (project) to the active one
    with active_phase(module, phases.IdeaSketchPhase):
        idea_sketch_factory(module=module)
        idea_sketch_factory(module=module)
        proposal_factory()

        view = views.IdeaListView.as_view()
        request = rf.get('/ideas')
        response = view(request)
        assert len(response.context_data['object_list']) == 2
        assert response.status_code == 200

        request = rf.get('/ideas/?status=proposal&project=')
        response = view(request)
        assert len(response.context_data['object_list']) == 1
        assert response.status_code == 200

        request = rf.get('/ideas/?idea_topics=environment&ordering=newest&'
                         'project=&status=')
        response = view(request)
        assert len(response.context_data['object_list']) == 3
        assert response.status_code == 200
