import uuid

import factory

from apps.invites.models import IdeaInvite
from tests.factories import UserFactory
from tests.ideas.factories import IdeaSketchFactory


class InviteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = IdeaInvite

    email = factory.Faker('email')
    token = factory.LazyFunction(uuid.uuid4)
    creator = factory.SubFactory(UserFactory)
    subject = factory.SubFactory(IdeaSketchFactory)
