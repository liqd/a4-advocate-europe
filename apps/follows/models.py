from django.db import models

from adhocracy4.models import base


class Follow(base.UserGeneratedContentModel):
    enabled = models.BooleanField(default=True)

    class Meta:
        unique_together = ('followable', 'creator')
        abstract = True

    def __repr__(self):
        return '{}({}, enabled={})'.format(
            self.__class__.__name__,
            self.followable,
            self.enabled
        )
