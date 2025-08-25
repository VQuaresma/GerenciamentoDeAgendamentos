from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Agenda
from .serializers import AgendaSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User

class AgendaViewSet(viewsets.ModelViewSet):
    serializer_class = AgendaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Agenda.objects.all()
        # Garante que cada usuário só veja suas próprias agendas
        return Agenda.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        # Salva o usuário logado ao criar a agenda
        serializer.save(usuario=self.request.user)

    @action(detail=True, methods=['post'])
    def cancelar(self, request, pk=None):
        agenda = self.get_object()
        if agenda.cancelada:
            return Response({"detail": "Agenda já está cancelada"}, status=status.HTTP_400_BAD_REQUEST)
        agenda.cancelada = True
        agenda.save()
        return Response({"detail": "Agenda cancelada com sucesso"})
    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializers_class = UserSerializer
    permission_classes = [IsAdminUser]