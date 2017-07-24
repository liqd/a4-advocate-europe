import pytest
from django.core.urlresolvers import reverse
from apps.ideas.models import IdeaSketch, IdeaSketchArchived, Proposal
from apps.ideas.phases import FullProposalPhase

from tests.helpers import active_phase


@pytest.mark.django_db
def test_proposal_anonymous_cannot_create_wizard(client,
                                                 idea_sketch_factory,
                                                 idea_factory):
    idea = idea_factory(visit_camp=True)
    idea_sketch = idea_sketch_factory(idea=idea)
    url = reverse('idea-sketch-add-proposal',
                  kwargs={'slug': idea_sketch.idea.slug})
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_proposal_random_user_cannot_create_wizard(client, user, idea_factory,
                                                   idea_sketch_factory):
    idea = idea_factory(visit_camp=True)
    idea_sketch = idea_sketch_factory(idea=idea)
    client.login(username=user.email,
                 password='password')
    url = reverse('idea-sketch-add-proposal',
                  kwargs={'slug': idea_sketch.idea.slug})

    with active_phase(idea_sketch.idea.module, FullProposalPhase):
        response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_proposal_no_camp_cannot_create_wizard(client, user, idea_factory,
                                               idea_sketch_factory):
    idea = idea_factory(visit_camp=False)
    idea.collaborators.add(user)
    idea_sketch = idea_sketch_factory(idea=idea)

    client.login(username=user.email,
                 password='password')
    url = reverse('idea-sketch-add-proposal',
                  kwargs={'slug': idea_sketch.idea.slug})

    with active_phase(idea_sketch.idea.module, FullProposalPhase):
        response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_proposal_no_phase_cannot_create_wizard(client, user, idea_factory,
                                                idea_sketch_factory):
    idea = idea_factory(visit_camp=True)
    idea_sketch = idea_sketch_factory(idea=idea)
    idea_sketch.collaborators.add(user)
    client.login(username=user.email,
                 password='password')
    url = reverse('idea-sketch-add-proposal',
                  kwargs={'slug': idea_sketch.idea.slug})

    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_proposal_collaborator_create_wizard(client, idea_factory,
                                             idea_sketch_factory, user, image):
    idea = idea_factory(idea_image=image, visit_camp=True)
    idea.collaborators.add(user)
    idea_sketch = idea_sketch_factory(idea=idea)

    client.login(username=user.email,
                 password='password')
    url = reverse('idea-sketch-add-proposal',
                  kwargs={'slug': idea_sketch.idea.slug})

    with active_phase(idea_sketch.idea.module, FullProposalPhase):

        assert IdeaSketchArchived.objects.all().count() == 0
        assert IdeaSketch.objects.all().count() == 1
        assert Proposal.objects.all().count() == 0

        # Form 1 (Applicant)
        response = client.get(url)
        wizard = response.context['wizard']
        assert response.status_code == 200
        assert wizard['steps'].count == 8
        assert wizard['steps'].step1 == 1
        for field, value in wizard['form'].initial.items():
            if hasattr(idea_sketch, field):
                assert str(value) == getattr(idea_sketch, field)
            else:
                assert str(value) == getattr(idea, field)
        data = {
            'proposal_create_wizard-current_step': '0'
        }
        for key, value in wizard['form'].initial.items():
            data['0-{}'.format(key)] = value

        # Form 2 (Partners)
        response = client.post(url, data)
        assert response.status_code == 200
        wizard = response.context['wizard']
        assert wizard['steps'].step1 == 2
        for field, value in wizard['form'].initial.items():
            if hasattr(idea_sketch, field):
                assert str(value) == getattr(idea_sketch, field)
            else:
                assert str(value) == getattr(idea, field)
        data = {
            'proposal_create_wizard-current_step': '1'
        }
        for key, value in wizard['form'].initial.items():
            data['1-{}'.format(key)] = value

        # Form 3 (Idea)
        response = client.post(url, data)
        assert response.status_code == 200
        wizard = response.context['wizard']
        assert wizard['steps'].step1 == 3
        for field, value in wizard['form'].initial.items():
            if type(value) is list:
                value = ','.join(value)
            if hasattr(idea_sketch, field):
                assert value == getattr(idea_sketch, field)
            else:
                assert value == getattr(idea, field)
        data = {
            'proposal_create_wizard-current_step': '2'
        }
        for key, value in wizard['form'].initial.items():
            data['2-{}'.format(key)] = value

        # Form 4 (Impact)
        response = client.post(url, data)
        assert response.status_code == 200
        wizard = response.context['wizard']

        assert wizard['steps'].step1 == 4

        for field, value in wizard['form'].initial.items():
            if type(value) is list:
                value = ','.join(value)
                if hasattr(idea_sketch, field):
                    assert value == getattr(idea_sketch, field)
                else:
                    assert value == getattr(idea, field)
        data = {
            'proposal_create_wizard-current_step': '3'
        }
        for key, value in wizard['form'].initial.items():
            data['3-{}'.format(key)] = value

        # Form 5 (Finances and Duration)
        response = client.post(url, data)
        assert response.status_code == 200
        wizard = response.context['wizard']
        assert wizard['steps'].step1 == 5

        data = {
            'proposal_create_wizard-current_step': '4',
            '4-selection_cohesion': 'Lorem ipsum ...',
            '4-selection_apart': 'Lorem ipsum ...',
            '4-selection_relevance': 'Lorem ipsum ...',
        }

        # Form 6 (Finances and Duration)
        response = client.post(url, data)
        assert response.status_code == 200
        wizard = response.context['wizard']
        assert wizard['steps'].step1 == 6

        data = {
            'proposal_create_wizard-current_step': '5',
            '5-total_budget': 6000,
            '5-budget_requested': 5000,
            '5-major_expenses': 'Lorem ipsum ...',
            '5-other_sources': 1,
            '5-other_sources_secured': 1,
            '5-duration': 24
        }

        # Form 7 (Community)
        response = client.post(url, data)
        assert response.status_code == 200
        wizard = response.context['wizard']
        assert wizard['steps'].step1 == 7

        for field, value in wizard['form'].initial.items():
            if hasattr(idea_sketch, field):
                assert value == getattr(idea_sketch, field)
            else:
                assert value == getattr(idea, field)

        data = {
            'proposal_create_wizard-current_step': '6',
            '6-accept_conditions': 'on'
        }

        for key, value in wizard['form'].initial.items():
            data['6-{}'.format(key)] = value

        # Form 8 (Finish)
        response = client.post(url, data)
        assert response.status_code == 200
        wizard = response.context['wizard']
        assert wizard['steps'].step1 == 8

        for field, value in wizard['form'].initial.items():
            if hasattr(idea_sketch, field):
                assert value == getattr(idea_sketch, field)
            else:
                assert value == getattr(idea, field)

        data = {
            'proposal_create_wizard-current_step': '7'
        }

        # Final Post
        response = client.post(url, data)
        assert response.status_code == 302
        assert Proposal.objects.all().count() == 1
        assert IdeaSketchArchived.objects.all().count() == 1
        assert IdeaSketch.objects.all().count() == 0

        new_proposal = Proposal.objects.all().first()
        idea_archive = new_proposal.idea_sketch_archived

        for field in IdeaSketchArchived._meta.get_all_field_names():
            if hasattr(idea_archive, field) and field != 'modified':
                archive_field = getattr(idea_archive, field)
                if type(archive_field) is list:
                    archive_field = (',').join(archive_field)
                    if hasattr(idea_sketch, field):
                        value = str(getattr(idea_sketch, field))
                        assert str(archive_field) == value
                    else:
                        value = str(getattr(idea_sketch.idea, field))
                        assert str(archive_field) == value

        assert Proposal.objects.all() \
            .first().idea.idea_title == idea_sketch.idea.idea_title
