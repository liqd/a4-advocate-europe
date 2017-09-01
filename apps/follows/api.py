from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from adhocracy4.api.permissions import RulesMethodMap, ViewSetRulesPermission

from . import Registry, serializers


class FollowViewSet(viewsets.ViewSet):
    """
    Get and update follows for current registered followable.
    """
    permission_classes = (ViewSetRulesPermission,)
    rules_method_map = RulesMethodMap(
        GET='{app_label}.view_{model_name}',
        OPTIONS='{app_label}.view_{model_name}',
        HEAD='{app_label}.view_{model_name}',
        POST=None,
        PUT='{app_label}.follow_{model_name}',
        PATCH='{app_label}.follow_{model_name}',
        DELETE=None,
    )
    lookup_field = 'pk'
    lookup_url_kwarg = None

    @property
    def queryset(self):
        return self.follow_model.objects

    @property
    def serializer_class(self):
        return serializers.get_serializer(self.follow_model)

    def dispatch(self, request, *args, **kwargs):
        self.follow_model = Registry.get_follow_model()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        """
        Get object that can be followed
        """
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        return get_object_or_404(self.follow_model.model, **filter_kwargs)

    def get_queryset(self):
        return self.follow_model.model.objects

    def get_follow_queryset(self):
        followable = self.get_object()
        queryset = self.queryset.filter(
            followable=followable
        )
        return queryset

    def retrieve(self, request, pk):
        """
        Retrives number of follows and follow state for current user.

        The pk parameter references the followable object, for which the count
        and the status is requested.
        """
        queryset = self.get_follow_queryset()
        response = Response({
            'follows': queryset.filter(enabled=True).count(),
        })

        if request.user.is_authenticated:
            user_follows = queryset.filter(
                creator=request.user,
                enabled=True,
            ).exists()
            response.data['enabled'] = user_follows

        return response

    def update(self, request, pk):
        """
        Create a new or update an existing follow.

        The pk parameter references the followable object, that should be
        followed or unfollowed.
        """
        queryset = self.get_follow_queryset().filter(
            creator=request.user
        )

        obj = queryset.first()
        serializer = self.serializer_class(
            obj,
            request.data,
            context={
                'request': request,
                'followable': self.get_object(),
            })

        serializer.is_valid(raise_exception=True)
        follow = serializer.save()

        return Response(
            {
                'follows': self.queryset.filter(enabled=True).count(),
                'enabled': follow.enabled
            },
            status=status.HTTP_200_OK if obj else status.HTTP_201_CREATED
        )
