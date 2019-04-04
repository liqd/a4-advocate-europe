import re

import pytest
from allauth.account.models import EmailAddress
from django.contrib import auth
from django.core import mail
from django.urls import reverse

from adhocracy4.test.helpers import redirect_target

User = auth.get_user_model()


@pytest.mark.django_db
def test_register(client, signup_url):
    assert EmailAddress.objects.count() == 0
    email = 'testuser@liqd.de'
    response = client.post(
        signup_url, {
            'username': 'testuser2',
            'email': email,
            'password1': 'password',
            'password2': 'password',
            'terms_of_use': 'on'
        }
    )
    assert response.status_code == 302
    assert EmailAddress.objects.filter(
        email=email, verified=False
    ).count() == 1
    assert len(mail.outbox) == 1
    confirmation_url = re.search(
        r'(http://testserver/.*/)',
        str(mail.outbox[0].body)
    ).group(0)

    confirm_email_response = client.get(confirmation_url)
    assert confirm_email_response.status_code == 200
    assert EmailAddress.objects.filter(
        email=email, verified=False
    ).count() == 1
    confirm_email_response = client.post(confirmation_url)
    assert confirm_email_response.status_code == 302
    assert EmailAddress.objects.filter(
        email=email, verified=True
    ).count() == 1


@pytest.mark.django_db
def test_register_with_next(client, signup_url):
    assert EmailAddress.objects.count() == 0
    email = 'testuser@liqd.de'
    response = client.post(
        signup_url, {
            'username': 'testuser2',
            'email': email,
            'password1': 'password',
            'password2': 'password',
            'terms_of_use': 'on',
            'next': '/ideas/pppp/',
        }
    )
    assert response.status_code == 302
    assert EmailAddress.objects.filter(
        email=email, verified=False
    ).count() == 1
    assert len(mail.outbox) == 1
    confirmation_url = re.search(
        r'(http://testserver/.*/?next=/ideas/pppp/)',
        str(mail.outbox[0].body)
    ).group(0)
    confirm_email_response = client.get(confirmation_url)
    assert confirm_email_response.status_code == 200
    assert EmailAddress.objects.filter(
        email=email, verified=False
    ).count() == 1
    confirm_email_response = client.post(confirmation_url)
    assert confirm_email_response.status_code == 302
    assert redirect_target(confirm_email_response) == "idea-detail"
    assert EmailAddress.objects.filter(
        email=email, verified=True
    ).count() == 1


@pytest.mark.django_db
def test_reset(client, user):
    user.emailaddress_set.create(email=user.email, verified=True)
    user.save()
    reset_req_url = reverse('account_reset_password')
    response = client.get(reset_req_url)
    assert response.status_code == 200
    response = client.post(reset_req_url, {'email': user.email})
    assert response.status_code == 302
    assert len(mail.outbox) == 1
    assert mail.outbox[0].to == [user.email]
    reset_url = re.search(
        r'(http://testserver/.*/)', str(mail.outbox[0].body)
    ).group(0)
    response = client.get(reset_url)
    assert response.status_code == 302
    reset_form_url = response.url
    response = client.get(reset_form_url)
    assert response.status_code == 200
    response = client.post(reset_form_url, {
        'password1': 'password1',
        'password2': 'password1',
    })
    assert response.status_code == 302
    assert response.url == '/'
    assert user.password != User.objects.get(username=user.username).password
