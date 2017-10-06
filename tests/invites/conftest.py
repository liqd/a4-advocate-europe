from pytest_factoryboy import register

from tests.ideas import factories as idea_factories
from tests.invites import factories as invite_factories

register(idea_factories.IdeaSketchFactory)
register(invite_factories.InviteFactory, 'invite')
