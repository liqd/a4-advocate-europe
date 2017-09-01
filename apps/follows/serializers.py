from rest_framework import serializers


class FollowableDefault:
    def set_context(self, serializer_field):
        self.context_value = serializer_field.context['followable']
        print(self.context_value)

    def __call__(self):
        return self.context_value

    def __repr__(self):
        return '{}()'.format(self.__class__.__name__, self.context_key)


class FollowSerializer(serializers.ModelSerializer):

    creator = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    followable = serializers.HiddenField(
        default=FollowableDefault()
    )

    class Meta:
        fields = ('creator', 'enabled', 'followable')
        extra_kwargs = {
            'enabled': {'required': True}
        }


def get_serializer(follow_model):
    meta = {
        'model': follow_model,
    }

    attrs = {
        'Meta': type('Meta', (FollowSerializer.Meta,), meta),
    }

    return serializers.SerializerMetaclass(
        follow_model.__name__ + 'FollowSerializer',
        (FollowSerializer,),
        attrs
    )
