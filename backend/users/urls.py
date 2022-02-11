from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import CustomUserViewSet
# from djoser.views import UserViewSet

app_name = 'api'

router = DefaultRouter()
router.register('users', CustomUserViewSet)
# router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
