import pytest
from django.core.urlresolvers import reverse

from apps.ideas.models import IdeaSketch, IdeaSketchArchived, Proposal
from apps.ideas.phases import FullProposalPhase
from tests.helpers import active_phase


@pytest.mark.django_db
def test_proposal_anonymous_cannot_create_wizard(client, idea_sketch_factory):
    idea_sketch = idea_sketch_factory(is_on_shortlist=True)
    url = reverse('idea-sketch-add-proposal',
                  kwargs={'slug': idea_sketch.slug})
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_proposal_random_user_cannot_create_wizard(client, user,
                                                   idea_sketch_factory):
    idea_sketch = idea_sketch_factory(is_on_shortlist=True)
    client.login(username=user.email,
                 password='password')
    url = reverse('idea-sketch-add-proposal',
                  kwargs={'slug': idea_sketch.slug})

    with active_phase(idea_sketch.module, FullProposalPhase):
        response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_proposal_no_camp_cannot_create_wizard(client, user,
                                               idea_sketch_factory):
    idea_sketch = idea_sketch_factory(is_on_shortlist=False)
    idea_sketch.co_workers.add(user)
    client.login(username=user.email,
                 password='password')
    url = reverse('idea-sketch-add-proposal',
                  kwargs={'slug': idea_sketch.slug})

    with active_phase(idea_sketch.module, FullProposalPhase):
        response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_proposal_no_phase_cannot_create_wizard(client, user,
                                                idea_sketch_factory):
    idea_sketch = idea_sketch_factory(is_on_shortlist=True)
    idea_sketch.co_workers.add(user)
    client.login(username=user.email,
                 password='password')
    url = reverse('idea-sketch-add-proposal',
                  kwargs={'slug': idea_sketch.slug})

    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_proposal_co_worker_create_wizard(client, idea_sketch_factory,
                                          user, image):
    idea_sketch = idea_sketch_factory(
        is_on_shortlist=True,
        idea_image=image,
        idea_title='Idea')
    idea_sketch.co_workers.add(user)
    client.login(username=user.email,
                 password='password')
    url = reverse('idea-sketch-add-proposal',
                  kwargs={'slug': idea_sketch.slug})

    with active_phase(idea_sketch.module, FullProposalPhase):

        assert IdeaSketchArchived.objects.all().count() == 0
        assert IdeaSketch.objects.all().count() == 1
        assert Proposal.objects.all().count() == 0

        # Form 1 (Applicant)
        response = client.get(url)
        wizard = response.context['wizard']
        assert response.status_code == 200
        assert wizard['steps'].count == 9
        assert wizard['steps'].step1 == 1
        for field, value in wizard['form'].initial.items():
            assert value == getattr(idea_sketch, field)
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
            assert str(value) == getattr(idea_sketch, field)
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
            assert value == getattr(idea_sketch, field)
        data = {
            'proposal_create_wizard-current_step': '2'
        }
        for key, value in wizard['form'].initial.items():
            if key == 'idea_title':
                data['2-{}'.format(key)] = value + ' Proposal'
            else:
                data['2-{}'.format(key)] = value

        # Form 4 (Impact)
        response = client.post(url, data)
        assert response.status_code == 200
        wizard = response.context['wizard']

        assert wizard['steps'].step1 == 4

        for field, value in wizard['form'].initial.items():
            if type(value) is list:
                value = ','.join(value)
            assert value == getattr(idea_sketch, field)
        data = {
            'proposal_create_wizard-current_step': '3'
        }
        for key, value in wizard['form'].initial.items():
            data['3-{}'.format(key)] = value

        # Form 5 (Selection)
        response = client.post(url, data)
        assert response.status_code == 200
        wizard = response.context['wizard']
        assert wizard['steps'].step1 == 5

        data = {
            'proposal_create_wizard-current_step': '4',
            '4-selection_advocating': 'Lorem ipsum ...',
            '4-selection_apart': 'Lorem ipsum ...',
            '4-selection_key_indicators': 'Lorem ipsum ...',
        }

        # Form 6 (Network)
        response = client.post(url, data)
        assert response.status_code == 200
        wizard = response.context['wizard']
        assert wizard['steps'].step1 == 6

        data = {
            'proposal_create_wizard-current_step': '5',
            '5-network': 'Lorem ipsum ...',
        }

        # Form 7 (Finances and Duration)
        response = client.post(url, data)
        assert response.status_code == 200
        wizard = response.context['wizard']
        assert wizard['steps'].step1 == 7

        data = {
            'proposal_create_wizard-current_step': '6',
            '6-total_budget': 6000,
            '6-budget_requested': 7000,
            '6-major_expenses': 'Lorem ipsum ...',
            '6-duration': 24
        }

        response = client.post(url, data)
        assert response.status_code == 200
        assert response.context['form'].errors == {'__all__':
                                                   ["The requested "
                                                    "budget can't "
                                                    "be higher than "
                                                    "the total "
                                                    "budget"]
                                                   }

        data = {
            'proposal_create_wizard-current_step': '6',
            '6-total_budget': 8000,
            '6-budget_requested': 7000,
            '6-major_expenses': 'Lorem ipsum ...',
            '6-other_sources': True,
            '6-other_sources_secured': True,
            '6-duration': 24
        }

        # Form 8 (Community)
        response = client.post(url, data)
        assert response.status_code == 200
        wizard = response.context['wizard']
        assert wizard['steps'].step1 == 8
        assert response.context['form'].errors == {}

        for field, value in wizard['form'].initial.items():
            assert value == getattr(idea_sketch, field)

        data = {
            'proposal_create_wizard-current_step': '7',
            '7-accept_conditions': 'on',
            '7-confirm_publicity': 'on',
            '7-confirm_idea_challenge_camp': 'on'
        }

        for key, value in wizard['form'].initial.items():
            data['7-{}'.format(key)] = value

        # Form 9 (Finish)
        response = client.post(url, data)
        assert response.status_code == 200
        wizard = response.context['wizard']
        assert wizard['steps'].step1 == 9

        for field, value in wizard['form'].initial.items():
            assert value == getattr(idea_sketch, field)

        data = {
            'proposal_create_wizard-current_step': '8'
        }

        # Final Post
        response = client.post(url, data)
        assert response.status_code == 302
        assert Proposal.objects.all().count() == 1
        assert IdeaSketchArchived.objects.all().count() == 1
        assert IdeaSketch.objects.all().count() == 1

        new_proposal = Proposal.objects.all().first()
        idea_archive = new_proposal.idea.idea_sketch_archived

        excluded_fields = [
            # is overwritten by update logic, due to explicit pk
            'modified',
            # only present with explicit one-to-one relations (like in archive)
            'idea_id',
        ]

        for field in IdeaSketchArchived._meta.get_fields():
            if field.name not in excluded_fields:
                archive_field = getattr(idea_archive, field.name)
                idea_sketch_field = getattr(idea_sketch, field.name)
                if field.name == 'idea':
                    archive_field = archive_field.proposal
                    idea_sketch_field = idea_sketch_field.proposal
                elif field.many_to_many or field.one_to_many:
                    archive_field = set(archive_field.all())
                    idea_sketch_field = set(idea_sketch_field.all())

                assert archive_field == idea_sketch_field

        proposal = Proposal.objects.all().first()
        assert proposal.idea_title == idea_sketch.idea_title + ' Proposal'
        assert proposal.is_on_shortlist
        assert proposal.slug == idea_sketch.idea.slug
