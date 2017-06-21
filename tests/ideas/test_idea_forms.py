import pytest

from django import forms

from apps.ideas import forms as idea_forms


@pytest.mark.django_db
@pytest.mark.parametrize('idea_sketch__collaborators', [[]])
def test_community_section_empty_edit(idea_sketch):
    """
    Check that the CommunitySectionEdit form works if no collaborators and
    and invites are present.
    """

    form = idea_forms.CommunitySectionEditForm(
        instance=idea_sketch,
    )

    assert list(form.collaborator_names) == []
    assert list(form.invite_emails) == []

    form = idea_forms.CommunitySectionEditForm(
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


@pytest.mark.django_db
@pytest.mark.parametrize('idea_sketch__invites',
                         [['test@test.de', 'foo@test.de']])
@pytest.mark.parametrize('idea_sketch__collaborators', [['Jürgen', 'Erich']])
def test_collaborator_edit(idea_sketch):
    """
    Remove collaborator and invite, while also adding new invite all in
    one operation.
    """
    collaborators = list(idea_sketch.collaborators.all())
    form = idea_forms.CommunitySectionEditForm(
        instance=idea_sketch,
    )

    assert list(form.collaborator_names) == [
        'Jürgen', 'Erich'
    ]
    assert list(form.invite_emails) == ['test@test.de', 'foo@test.de']

    form = idea_forms.CommunitySectionEditForm(
        instance=idea_sketch,
        data={
            'collaborators_emails': 'test1@test.de, test2@test.de',
            'invites': ['test1@test.de']
        }
    )
    assert not form.is_valid()

    form = idea_forms.CommunitySectionEditForm(
        instance=idea_sketch,
        data={
            'collaborators_emails': 'test1@test.de, test2@test.de',
            'invites': ['foo@test.de'],
            'collaborators': ['Erich'],
            'reach_out': 'edit_reach_out',
            'how_did_you_hear': 'other'
        }
    )

    form.is_valid()
    assert not form.errors
    idea_sketch = form.save()
    assert idea_sketch.reach_out == 'edit_reach_out'
    invites = ['foo@test.de', 'test1@test.de', 'test2@test.de']
    new_invites = list(
        idea_sketch.ideainvite_set.values_list('email', flat=True)
    )
    assert invites == new_invites
    assert list(idea_sketch.collaborators.all()) == collaborators[1:]


@pytest.mark.django_db
@pytest.mark.parametrize('idea_sketch__invites',
                         [['test1@test.de', 'test2@test.de', 'test3@test.de']])
@pytest.mark.parametrize('idea_sketch__collaborators', [['test4', 'test5']])
def test_collaborator_edit_too_many(idea_sketch):
    form = idea_forms.CommunitySectionEditForm(
        instance=idea_sketch,
        data={
            'collaborators_emails': 'test6@test.de',
            'reach_out': 'edit_reach_out',
            'how_did_you_hear': 'other',
            'invites': ['test1@test.de', 'test2@test.de', 'test3@test.de'],
            'collaborators': ['test4', 'test5'],
        }
    )

    assert not form.is_valid()


@pytest.mark.django_db
@pytest.mark.parametrize('idea_sketch__invites',
                         [['test1@test.de', 'test2@test.de', 'test3@test.de']])
@pytest.mark.parametrize('idea_sketch__collaborators', [['test4', 'test5']])
def test_collaborator_edit_replace_one(idea_sketch):
    form = idea_forms.CommunitySectionEditForm(
        instance=idea_sketch,
        data={
            'collaborators_emails': 'test6@test.de',
            'reach_out': 'edit_reach_out',
            'how_did_you_hear': 'other',
            'invites': ['test1@test.de', 'test2@test.de', 'test3@test.de'],
            'collaborators': ['test4'],
        }
    )

    assert form.is_valid()


@pytest.mark.django_db
@pytest.mark.parametrize('idea_sketch__invites', [['test@test.de']])
def test_collaborters_reinvite(idea_sketch):
    form = idea_forms.CommunitySectionEditForm(
        instance=idea_sketch,
        data={
            'collaborators_emails': 'test@test.de',
            'reach_out': 'edit_reach_out',
            'how_did_you_hear': 'other',
            'invites': ['test@test.de'],
        }
    )

    assert not form.is_valid()


def test_clean_collaborators_email():

    class TestForm(idea_forms.CollaboratorsEmailsFormMixin, forms.Form):
        collaborators_emails = forms.CharField()

    form = TestForm(
        data={'collaborators_emails': 'meg@test.com, carren@test.de'}
    )
    assert form.is_valid()

    form = TestForm(data={'collaborators_emails': 'meg, carren@test.de, john'})
    assert not form.is_valid()
    assert form.errors == {
        'collaborators_emails': [
            'Invalid email address (meg)',
            'Invalid email address (john)'
        ]
    }

    form = TestForm(
        data={'collaborators_emails': 'carren@test.de, carren@test.de'}
    )
    assert not form.is_valid()
    assert form.errors == {
        'collaborators_emails': [
            'Duplicate email address (carren@test.de)',
        ]
    }
