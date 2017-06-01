from pytest_factoryboy import register
from tests.ideas import factories as idea_factories

register(idea_factories.IdeaSketchFactory)
register(idea_factories.ProposalFactory)
register(idea_factories.IdeaSketchArchivedFactory)
