from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (RecipeViewSet, IngredientViewSet, TagViewSet,
                    RecipeDownloadViewSet,
                    UserViewSet,
                    # #UserMeViewSet, UserSPViewSet
                    )

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet, basename='recipes',)
router.register(r'recipes/download_shopping_cart', RecipeDownloadViewSet, basename='recipes_download',)

router.register(r'users', UserViewSet, basename='users',)

router.register(r'tags', TagViewSet, basename='tags',)
router.register(r'ingredients', IngredientViewSet, basename='ingredients',)

urlpatterns = [
    path('', include(router.urls)),
]
