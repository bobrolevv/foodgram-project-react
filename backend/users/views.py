from recipes.models import Subsription, User
from rest_framework import viewsets, permissions, filters
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.pagination import PageNumberPagination

from api.permissions import IsAuthorOrReadOnlyPermission as P
from .serializers import SubsriptionSerializer


class SubsribeViewSet(viewsets.ModelViewSet):
    pass


class SubsriptionViewSet(
                    viewsets.ModelViewSet
                    # CreateModelMixin,
                    # ListModelMixin,
                    # viewsets.GenericViewSet
                    ):
    serializer_class = SubsriptionSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['user__username', 'author__username']
    # queryset = User.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # queryset = User.objects.all()
        queryset = Subsription.objects.all()
        user = self.request.user
        return queryset.filter(user=user)


