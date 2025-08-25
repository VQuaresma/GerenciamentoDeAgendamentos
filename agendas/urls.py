from rest_framework.routers import DefaultRouter
from .views import AgendaViewSet, UserViewSet

router = DefaultRouter()
router.register(r'agendas', AgendaViewSet, basename='agenda')
router.register(r'usuarios', UserViewSet, basename='usuarios')

urlpatterns = router.urls
