from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (RecipeViewSet,
                    RecipeDownloadViewSet,
                    TagViewSet,
                    IngredientViewSet,
                    )

from users.views import SubsriptionViewSet, SubsribeViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet, basename='recipes',)
router.register(r'recipes/download_shopping_cart', RecipeDownloadViewSet, basename='recipes_download',)
router.register(r'tags', TagViewSet, basename='tags',)
router.register(r'ingredients', IngredientViewSet, basename='ingredients',)
router.register('users/subscriptions', SubsriptionViewSet, basename='subscriptions',)
router.register('users/<id>/subscribe', SubsribeViewSet, basename='subscribe',)


urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    # path('', include(router.urls)),
]
