from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubsriptionViewSet


router = DefaultRouter()
router.register(r'sub', SubsriptionViewSet, basename='sub',)

urlpatterns = [
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),

]
