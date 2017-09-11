import factory
import pytest
from django.core.urlresolvers import reverse
from pytest_factoryboy import register
from rest_framework.test import APIClient

from adhocracy4.test import factories as a4factories
from adhocracy4.test import helpers

from . import factories


register(factories.UserFactory)
register(factories.UserFactory, 'user2')
register(factories.AdminFactory, 'admin')

register(a4factories.OrganisationFactory)
register(a4factories.ProjectFactory)
register(a4factories.ModuleFactory)
register(a4factories.PhaseFactory)


def pytest_configure(config):
    # Patch email background_task decorators for all tests
    helpers.patch_background_task_decorator('adhocracy4.emails.tasks')


@pytest.fixture
def image():
    return factory.django.ImageField(width=1400, height=1400)


@pytest.fixture
def apiclient():
    return APIClient()


@pytest.fixture
def signup_url():
    return reverse('account_signup')
