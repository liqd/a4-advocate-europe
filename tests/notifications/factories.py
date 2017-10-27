import factory

from tests.factories import UserFactory
from tests.ideas.factories import IdeaSketchFactory


class CommentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'a4comments.Comment'

    comment = factory.Faker('text')
    content_object = factory.SubFactory(IdeaSketchFactory)
    creator = factory.SubFactory(UserFactory)
