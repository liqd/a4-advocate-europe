import factory
import pytest
from pytest_factoryboy import register

from . import factories

register(factories.UserFactory)
register(factories.UserFactory, 'user2')
register(factories.AdminFactory, 'admin')


@pytest.fixture
def image():
    return factory.django.ImageField(width=1400, height=1400)
