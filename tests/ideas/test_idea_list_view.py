import pytest
from django.core.urlresolvers import reverse

from apps.ideas import phases

from tests.helpers import active_phase


@pytest.mark.django_db
def test_idea_list_view(client, idea_sketch_factory, proposal_factory):
    idea_sketch_factory()
    idea_sketch_factory()
    proposal_factory()

    url = reverse('idea-sketch-list')
    response = client.get(url)
    # default filter settings for the idea filters are 'status': 'winner'
    assert len(response.context_data['object_list']) == 0
    assert response.status_code == 200

    response = client.get(url + '?status=proposal')
    assert len(response.context_data['object_list']) == 1
    assert response.status_code == 200

    response = client.get(url + '?idea_topics=environment&ordering=newest&'
                          'project=&status=')
    assert len(response.context_data['object_list']) == 3
    assert response.status_code == 200


@pytest.mark.django_db
def test_idea_list_view_idea_sketch_phase(client, admin, idea_sketch_factory,
                                          proposal_factory, module):
    url = reverse('idea-sketch-list')

    # the default filters for the ideaSketchPhase set
    # 'status': 'idea_sketch' and the year (project) to the active one
    with active_phase(module, phases.IdeaSketchPhase):
        idea_sketch_factory(module=module)
        idea_sketch_factory(module=module)
        proposal_factory()

        response = client.get(url)
        assert len(response.context_data['object_list']) == 2
        assert response.status_code == 200

        response = client.get(url + '?status=proposal&project=')
        assert len(response.context_data['object_list']) == 1
        assert response.status_code == 200

        response = client.get(url + '?idea_topics=environment&ordering=newest&'
                              'project=&status=')
        assert len(response.context_data['object_list']) == 3
        assert response.status_code == 200
