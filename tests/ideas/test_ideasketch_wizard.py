import pytest
from django.core import mail
from django.core.urlresolvers import reverse

from apps.ideas.models import IdeaSketch
from apps.ideas.phases import IdeaSketchPhase
from tests.helpers import active_phase


@pytest.mark.django_db
def test_ideasketch_create_wizard(client, user, module):
    client.login(username=user.email,
                 password='password')
    url = reverse('idea-sketch-create',
                  kwargs={'slug': module.slug})

    with active_phase(module, IdeaSketchPhase):

        # Form 1 (Applicant)
        response = client.get(url)
        assert response.status_code == 200

        data = {
            'idea_sketch_create_wizard-current_step': '0',

            '0-first_name': 'Qwertz',
            '0-last_name': 'Uiopü',
            '0-organisation_status': 'other',
        }

        response = client.post(url, data)
        assert response.context['form'].errors == {'organisation_status_extra':
                                                   ["You selected 'other' as "
                                                    "organisation status. "
                                                    "Please provide more "
                                                    "information about your "
                                                    "current status."]}
        assert response.status_code == 200

        data = {
            'idea_sketch_create_wizard-current_step': '0',
            '0-organisation_status_extra': 'We are great',
            '0-first_name': 'Qwertz',
            '0-last_name': 'Uiopü',
            '0-organisation_status': 'other',
        }

        # Form 2 (Partners)
        response = client.post(url, data)
        assert response.context['form'].errors == {}
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
            '2-idea_location': 'ruhr_linkage'
        }

        response = client.post(url, data)
        assert response.context['form'].errors == {'idea_location_ruhr':
                                                   ['You indicated '
                                                    'that your idea '
                                                    'links to '
                                                    'the Ruhr area '
                                                    'of Germany. '
                                                    'Please specify.']}

        assert response.status_code == 200

        data = {
            'idea_sketch_create_wizard-current_step': '2',

            '2-idea_title': 'My very good idea',
            '2-idea_pitch': 'My very good idea is such a good idea!',
            '2-idea_topics': 'education',
            '2-idea_location': 'ruhr_linkage',
            '2-idea_location_ruhr': 'Our project will take place in Essen'
        }

        # Form 4 (Impact)
        response = client.post(url, data)
        assert response.context['form'].errors == {}
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

        # Form 5 (Idea Challenge camp)
        response = client.post(url, data)
        assert response.status_code == 200

        data = {
            'idea_sketch_create_wizard-current_step': '4',

            '4-idea_challenge_camp_option': 'not_sure',
            '4-idea_challenge_camp_represent': 'Mr. Not So Sure',
            '4-idea_challenge_camp_email': 'email@example.com',
            '4-idea_challenge_camp_benefit': 'We will be very sure afterwards',
        }

        # Form 6 (Community)
        response = client.post(url, data)
        assert response.status_code == 200

        data = {
            'idea_sketch_create_wizard-current_step': '5',

            '5-how_did_you_hear': 'personal_contact',
            '5-accept_conditions': True,
            '5-confirm_publicity': True,
            '5-confirm_idea_challenge_camp': True
        }

        # Form 7 (Finish)
        response = client.post(url, data)
        assert response.status_code == 200
        assert IdeaSketch.objects.all().count() == 0

        data = {
            'idea_sketch_create_wizard-current_step': '6',
        }

        response = client.post(url, data)
        my_idea_sketch = IdeaSketch.objects.get(idea_title='My very good idea')

        assert response.status_code == 302
        assert IdeaSketch.objects.all().count() == 1
        assert my_idea_sketch.first_name == 'Qwertz'
        assert (my_idea_sketch.get_idea_location_display() ==
                'Links to the Ruhr area of Germany')
        assert my_idea_sketch.target_group == 'Children'
        assert mail.outbox[0].subject == (
            'Thank you for submitting your project idea for the '
            'Advocate Europe idea challenge!'
        )
        assert mail.outbox[0].recipients() == [user.email]
