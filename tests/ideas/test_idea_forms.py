import pytest

from apps.ideas import forms


@pytest.mark.django_db
@pytest.mark.parametrize('idea_sketch__collaborators', [[]])
def test_community_section_empty_edit(idea_sketch):
    """
    Check that the CommunitySectionEdit form works if no collaborators and
    and invites are present.
    """

    form = forms.CommunitySectionEditForm(
        instance=idea_sketch,
    )

    assert list(form.collaborator_names) == []
    assert list(form.invite_emails) == []

    form = forms.CommunitySectionEditForm(
        instance=idea_sketch,
        data={
            'collaborators_emails': 'test@test.de, test2@test.de',
            'reach_out': 'edit_reach_out',
            'how_did_you_hear': 'other'
        }
    )

    assert form.is_valid()
    idea_sketch = form.save()
    assert idea_sketch.reach_out == 'edit_reach_out'
    assert idea_sketch.how_did_you_hear == 'other'
    invites = ['test@test.de', 'test2@test.de']
    new_invites = list(
        idea_sketch.ideainvite_set.values_list('email', flat=True)
    )
    assert new_invites == invites
