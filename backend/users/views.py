from recipes.models import Subsription
from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination

from api.permissions import IsAuthorOrReadOnlyPermission as P
from .serializers import SubsriptionSerializer
# from djoser.views import UserViewSet

class SubsriptionViewSet(viewsets.ModelViewSet):
    queryset = Subsription.objects.all()
    serializer_class = SubsriptionSerializer


# class FollowViewSet(CreateModelMixin,
#                     ListModelMixin,
#                     viewsets.GenericViewSet):
#     serializer_class = FollowSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['user__username', 'following__username']
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#     def get_queryset(self):
#         queryset = Follow.objects.all()
#         user = self.request.user
#         return queryset.filter(following=user)


