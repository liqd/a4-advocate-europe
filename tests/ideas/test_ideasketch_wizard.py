import pytest
from django.core.urlresolvers import reverse
from apps.ideas.models import IdeaSketch
from apps.ideas.phases import IdeaSketchPhase

from tests.helpers import active_phase


@pytest.mark.django_db
def test_ideasketch_create_wizard(client, user,
                                  idea_sketch_factory):
    idea_sketch = idea_sketch_factory()
    client.login(username=user.email,
                 password='password')
    url = reverse('idea-sketch-create',
                  kwargs={'slug': idea_sketch.module.slug})

    with active_phase(idea_sketch.module, IdeaSketchPhase):

        # Form 1 (Applicant)
        response = client.get(url)
        assert response.status_code == 200

        data = {
            'idea_sketch_create_wizard-current_step': '0',

            '0-first_name': 'Qwertz',
            '0-last_name': 'Uiopü',
            '0-organisation_status': 'no_non_profit',
        }

        # Form 2 (Partners)
        response = client.post(url, data)
        assert response.status_code == 200

        data = {
            'idea_sketch_create_wizard-current_step': '1',
        }

        # Form 3 (Idea details)
        response = client.post(url, data)
        assert response.status_code == 200

        data = {
            'idea_sketch_create_wizard-current_step': '2',

            '2-idea_title': 'My very good idea',
            '2-idea_pitch': 'My very good idea is such a good idea!',
            '2-idea_topics': 'education',
            '2-idea_location': 'ruhr_linkage',
        }

        # Form 4 (Impact)
        response = client.post(url, data)
        assert response.status_code == 200

        data = {
            'idea_sketch_create_wizard-current_step': '3',

            '3-challenge': 'Balance a ball on your nose',
            '3-outcome': 'I balanced a ball on my nose',
            '3-plan': 'I will balance a ball on my nose',
            '3-importance': 'That is only important to me',
            '3-target_group': 'Children',
            '3-members': 'Me and my ball',
        }

        # Form 5 (Collaboration camp)
        response = client.post(url, data)
        assert response.status_code == 200

        data = {
            'idea_sketch_create_wizard-current_step': '4',

            '4-collaboration_camp_option': 'not_sure',
            '4-collaboration_camp_represent': 'Mr. Not So Sure',
            '4-collaboration_camp_email': 'email@example.com',
            '4-collaboration_camp_benefit': 'We will be very sure afterwards',
        }

        # Form 6 (Collaboration camp)
        response = client.post(url, data)
        assert response.status_code == 200
        assert IdeaSketch.objects.all().count() == 1

        data = {
            'idea_sketch_create_wizard-current_step': '5',

            '5-how_did_you_hear': 'personal_contact',
            '5-accept_conditions': True
        }

        response = client.post(url, data)
        my_idea_sketch = IdeaSketch.objects.get(idea_title='My very good idea')

        assert response.status_code == 302
        assert IdeaSketch.objects.all().count() == 2
        assert my_idea_sketch.first_name == 'Qwertz'
        assert (my_idea_sketch.get_idea_location_display() ==
                'Linkage to the Ruhr area of Germany')
        assert my_idea_sketch.target_group == 'Children'
        assert my_idea_sketch.collaboration_camp_option == 'not_sure'
