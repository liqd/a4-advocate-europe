import pytest
from django.core.urlresolvers import reverse
from apps.ideas.models import IdeaSketch, IdeaSketchArchived, Proposal


@pytest.mark.django_db
def test_proposal_anonymous_cannot_create_wizard(client, idea_sketch_factory):
    idea_sketch = idea_sketch_factory(visit_camp=False)
    url = reverse('idea-sketch-add-proposal',
                  kwargs={'slug': idea_sketch.slug})
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_proposal_admin_create_wizard(client,
                                      idea_sketch_factory, admin, image):
    idea_sketch = idea_sketch_factory(visit_camp=False, idea_image=image)
    client.login(username=admin.email,
                 password='password')
    url = reverse('idea-sketch-add-proposal',
                  kwargs={'slug': idea_sketch.slug})

    assert IdeaSketchArchived.objects.all().count() == 0
    assert IdeaSketch.objects.all().count() == 1
    assert Proposal.objects.all().count() == 0

    # Form 1 (Applicant)
    response = client.get(url)
    wizard = response.context['wizard']
    assert response.status_code == 200
    assert wizard['steps'].count == 6
    assert wizard['steps'].step1 == 1
    for field, value in wizard['form'].initial.items():
        assert str(value) == getattr(idea_sketch, field)
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
        if type(value) is list:
            value = ','.join(value)
        assert value == getattr(idea_sketch, field)
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
        assert value == getattr(idea_sketch, field)
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
        '4-total_budget': 6000,
        '4-budget_requested': 5000,
        '4-major_expenses': 'Lorem ipsum ...',
        '4-other_sources': 1,
        '4-other_sources_secured': 1,
        '4-duration': 24
    }

    # Form 6 (Community)
    response = client.post(url, data)
    assert response.status_code == 200
    wizard = response.context['wizard']
    assert wizard['steps'].step1 == 6

    for field, value in wizard['form'].initial.items():
        assert value == getattr(idea_sketch, field)

    data = {
        'proposal_create_wizard-current_step': '5',
        '5-accept_conditions': 'on'
    }

    for key, value in wizard['form'].initial.items():
        data['5-{}'.format(key)] = value

    # Final Post
    response = client.post(url, data)
    assert response.status_code == 302
    assert Proposal.objects.all().count() == 1
    assert IdeaSketchArchived.objects.all().count() == 1
    assert IdeaSketch.objects.all().count() == 1

    new_proposal = Proposal.objects.all().first()
    idea_archive = new_proposal.idea_sketch_archived

    for field in IdeaSketchArchived._meta.get_all_field_names():
        if hasattr(idea_archive, field) and field != 'modified':
            archive_field = getattr(idea_archive, field)
            if type(archive_field) is list:
                archive_field = (',').join(archive_field)
            idea_sketch_field = getattr(idea_sketch, field)
            assert str(archive_field) == str(idea_sketch_field)

    assert Proposal.objects.all().first().idea_title == idea_sketch.idea_title
