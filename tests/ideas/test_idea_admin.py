import pytest
from django.core.urlresolvers import reverse


@pytest.mark.django_db
def test_idea_admin_actions(client, admin, idea_sketch_factory,
                            proposal_factory):
    is1 = idea_sketch_factory()
    is2 = idea_sketch_factory()
    # pr = proposal_factory()

    login = client.login(email=admin.email, password='password')
    assert login
    change_url = reverse('admin:advocate_europe_ideas_idea_changelist')

    data = {
        'action': 'set_visit_camp_true',
        '_selected_action': [is1.pk, is2.pk]
        }
    response = client.post(change_url, data)

    is1.refresh_from_db()
    is2.refresh_from_db()

    assert response.status_code == 302
    assert is1.visit_camp
    assert is2.visit_camp
