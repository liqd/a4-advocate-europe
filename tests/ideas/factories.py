import factory

from adhocracy4.test.factories import ModuleFactory
from apps.ideas.models import Idea, IdeaSketch, IdeaSketchArchived, Proposal
from tests.factories import UserFactory


class IdeaSketchFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = IdeaSketch

    first_name = factory.Faker('first_name_female')
    last_name = factory.Faker('last_name')
    organisation_status = 'non_profit'
    year_of_registration = 2002
    idea_location = ['online']
    idea_topics = ['environment', 'social_inclusion']
    idea_pitch = factory.Faker('text')
    challenge = factory.Faker('text')
    importance = factory.Faker('text')
    outcome = factory.Faker('text')
    members = 'admin@liqd.de, user@liqd.de'
    target_group = factory.Faker('text')
    plan = factory.Faker('text')
    how_did_you_hear = 'websites'

    idea_title = factory.Faker('name')
    creator = factory.SubFactory(UserFactory)
    module = factory.SubFactory(ModuleFactory)

    @factory.post_generation
    def co_workers(self, create, extracted, **kwargs):
        if extracted == []:
            return

        if not extracted:
            user = UserFactory()
            self.co_workers.add(user)
            return

        if extracted:
            for user in extracted:
                if isinstance(user, str):
                    self.co_workers.add(
                        UserFactory(username=user)
                    )
                else:
                    self.co_workers.add(user)

    @factory.post_generation
    def invites(self, create, extracted, **kwargs):
        if not extracted:
            return

        if extracted:
            for email in extracted:
                self.ideainvite_set.invite(
                    creator=self.creator,
                    email=email,
                )


class IdeaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Idea


class IdeaSketchArchivedFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = IdeaSketchArchived

    creator = factory.SubFactory(UserFactory)
    idea = factory.SubFactory(IdeaFactory)


class ProposalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Proposal

    idea_title = factory.Faker('name')
    creator = factory.SubFactory(UserFactory)
    module = factory.SubFactory(ModuleFactory)
    network = factory.Faker('text')
    selection_advocating = factory.Faker('text')
    selection_key_indicators = factory.Faker('text')
    idea_topics = 'environment'
    total_budget = factory.Faker('random_number')
    budget_requested = factory.Faker('random_number')
    duration = factory.Faker('random_number')
    is_on_shortlist = True

    @factory.post_generation
    def co_workers(self, create, extracted, **kwargs):
        if not extracted:
            user = UserFactory()
            self.co_workers.add(user)
            return

        if extracted:
            for user in extracted:
                self.co_workers.add(user)

    @factory.post_generation
    def idea_archive(self, create, extracted, **kwargs):
        assert not extracted
        self.ideasketcharchived = IdeaSketchArchivedFactory(
            creator=self.creator,
            idea=self.idea,
        )
