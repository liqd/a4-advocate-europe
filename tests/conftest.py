import factory
import pytest
from pytest_factoryboy import register

from adhocracy4.test import factories as a4factories

from . import factories


register(factories.UserFactory)
register(factories.UserFactory, 'user2')
register(factories.AdminFactory, 'admin')

register(a4factories.OrganisationFactory)
register(a4factories.ProjectFactory)
register(a4factories.ModuleFactory)
register(a4factories.PhaseFactory)


@pytest.fixture
def image():
    return factory.django.ImageField(width=1400, height=1400)
