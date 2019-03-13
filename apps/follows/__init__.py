from django.db import models
from django.db.models.base import ModelBase

default_app_config = 'apps.follows.apps.Config'


class Registry:
    """
    Holds all current follow implementations.

    Could be extend to hold more than a single instance at a time.
    """
    _follow_model = None

    @classmethod
    def get_follow_model(cls):
        return cls._follow_model

    @classmethod
    def _create_follow_class(cls, name, target_model):
        attrs = {
            'followable': models.ForeignKey(target_model, editable=False),
            '__module__': target_model.__module__,
            'model': target_model,
        }

        from .models import Follow
        return ModelBase(name.title() + 'Follow', (Follow,), attrs)

    @classmethod
    def register_follow(cls, target_model):
        name = target_model._meta.model_name
        cls._follow_model = cls._create_follow_class(name, target_model)


register_follow = Registry.register_follow
