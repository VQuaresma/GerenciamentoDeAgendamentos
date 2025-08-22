from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HomeViewSet

router = DefaultRouter()
router.register(r'home', HomeViewSet, basename='nome')

urlpatterns = [
    path('', include(router.urls)),
]