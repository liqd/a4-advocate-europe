from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from . import Registry, serializers


class FollowViewSet(viewsets.ViewSet):
    """
    Get and update follows for current registered followable.

    TODO:
    - permissions
    """
    def dispatch(self, request, *args, **kwargs):
        self.follow_model = Registry.get_follow_model()
        return super().dispatch(request, *args, **kwargs)

    @property
    def queryset(self):
        return self.follow_model.objects

    @property
    def serializer_class(self):
        return serializers.get_serializer(self.follow_model)

    def get_followable(self, pk):
        """
        Get object that can be followed
        """
        return get_object_or_404(self.follow_model.model, pk=pk)

    def get_queryset(self, followable_pk):
        followable = self.get_followable(followable_pk)
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
        queryset = self.get_queryset(pk)
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
        queryset = self.get_queryset(pk).filter(
            creator=request.user
        )

        obj = queryset.first()
        serializer = self.serializer_class(
            obj,
            request.data,
            context={
                'request': request,
                'followable': self.get_followable(pk),
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
