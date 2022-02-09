from recipes.models import Recipe, Ingredient, Tag, User
from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination

from .permissions import IsAuthorOrReadOnlyPermission as P
from .serializers import RecipeSerializer, IngredientSerializer, TagSerializer, UserSerializer
# from djoser.views import UserViewSet

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    pagination_class = PageNumberPagination
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('pub_date',)
    ordering = ('-pub_date',)
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, P)


class RecipeDownloadViewSet(viewsets.ModelViewSet):
    pass


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    pagination_class = None


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None


