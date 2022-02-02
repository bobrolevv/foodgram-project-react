from rest_framework import viewsets, permissions

from recipes.models import Recipe, Ingredient, Tag, User, IngredientRecipe
from .serializers import RecipeSerializer, IngredientSerializer, TagSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnlyPermission as P


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, P)


class RecipeDownloadViewSet(viewsets.ModelViewSet):
    pass


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, P)


# class UserMeViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, P)


# class UserSPViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, P)