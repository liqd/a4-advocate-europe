import pytest
from django.core.urlresolvers import reverse


@pytest.mark.django_db
def test_idea_admin_actions(client, admin, idea_sketch_factory,
                            proposal_factory):
    is1 = idea_sketch_factory()
    is2 = idea_sketch_factory()
    # pr = proposal_factory()

    client.login(email=admin.email, password='password')
    change_url = reverse('admin:advocate_europe_ideas_idea_changelist')

    data = {
        'action': 'set_visit_camp_true',
        '_selected_action': [is1, is2]
        }
    response = client.post(change_url, data)

    # import pdb; pdb.set_trace()
    assert response.status_code == 200
    # assert response.context['user'] == admin
    # assert is1.visit_camp == True
    # assert is2.visit_camp == True
