from django.utils.translation import ugettext_lazy as _

from adhocracy4 import phases

from . import apps, models


class DummyPhase(phases.PhaseContent):
    app = apps.IdeasConfig.label
    phase = 'dummy'
    weight = 10
    view = ''

    name = _('Dummy phase')
    description = _('Do nothing.')
    module_name = _('Dummy')

    features = {
        'crud': (models.IdeaSketch,),
    }

phases.content.register(DummyPhase())
