from autofixture import AutoFixture, register
from faker import Factory

from .models import IdeaSketch

fake = Factory.create()


class IdeaSketchAutoFixture(AutoFixture):

    follow_pk = True
    follow_fk = True


register(IdeaSketch, IdeaSketchAutoFixture)
