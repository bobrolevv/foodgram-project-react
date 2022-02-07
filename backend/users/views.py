from recipes.models import Subsription
from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination

from api.permissions import IsAuthorOrReadOnlyPermission as P
from .serializers import SubsriptionSerializer
# from djoser.views import UserViewSet

class SubsriptionViewSet(viewsets.ModelViewSet):
    queryset = Subsription.objects.all()
    serializer_class = SubsriptionSerializer




