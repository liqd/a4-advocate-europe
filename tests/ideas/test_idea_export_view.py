import pytest
from django.core.exceptions import PermissionDenied

from apps.ideas import views


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
    # the default filters without an active phase set 'status': 'winner'
    idea_sketch_factory(is_winner=True)
    proposal_factory(is_winner=True)
    proposal_factory(is_winner=True)

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
