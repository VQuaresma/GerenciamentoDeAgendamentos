from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Agenda
from .serializers import AgendaSerializer, UserSerializer
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
class AgendaViewSet(viewsets.ModelViewSet):
    serializer_class = AgendaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = Agenda.objects.filter(excluido=False)
        if user.is_staff:
            return qs
        return qs.filter(usuario=user)

    @swagger_auto_schema(
            operation_description="Cria uma nova agenda para o usuario logado",
            request_body=AgendaSerializer,
            responses={201: AgendaSerializer}
    )
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    @swagger_auto_schema(
            operation_description="Cancela uma agenda específica."
    )
    @action(detail=True, methods=['post'])
    def cancelar(self, request, pk=None):
        agenda = self.get_object()
        if agenda.status == "cancelado":
            return Response({"detail": "Agenda já está cancelada"}, status=status.HTTP_400_BAD_REQUEST)
        agenda.cancelada = True
        agenda.save()
        return Response({"detail": "Agenda cancelada com sucesso"})
    
    @swagger_auto_schema(
            operation_description="Atualiza o status de uma agenda ( somente users com admin)",
            request_body=AgendaSerializer
    )
    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def atualizar_status(self, request, pk=None):
        agenda = self.get_object()
        novo_status = request.data.get("status")

        if novo_status not in ["pendente", "marcado", "cancelado"]:
            return Response({"detail": "Status inválido"}, status=status.HTTP_400_BAD_REQUEST)

        agenda.status = novo_status
        agenda.save()
        return Response({"detail": f"Status atualizado para {agenda.status}"})


    @swagger_auto_schema(
            operation_description="Exclui por softdelete uma agenda."
    )
    @action(detail=True, methods=['post'])
    def excluir(self, request, pk=None):
        agenda = self.get_object()
        agenda.excluido = True
        agenda.save()
        return Response({"detail": "Agenda movida para excluídos."})
    

    @swagger_auto_schema(
            operation_description="Lista todas as agendas excluidas (somente adiministradores)"
    )
    @action(detail=False, methods=['get'], permission_classes=[IsAdminUser])
    def excluidos(self, request):
        agendas = Agenda.objects.filter(excluido=True)
        serializer = self.get_serializer(agendas, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
            operation_description="Restaura uma aenda excluida (somente adiministradores)"
    )
    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def restaurar(self, request, pk=None):
    # Busca a agenda mesmo que esteja excluída
        try:
            agenda = Agenda.objects.get(pk=pk, excluido=True)
        except Agenda.DoesNotExist:
            return Response({"detail": "Agenda não está excluída ou não existe."}, status=status.HTTP_400_BAD_REQUEST)

        agenda.excluido = False
        agenda.save()
        return Response({"detail": "Agenda restaurada com sucesso."})
    
    def get_serializer(self, *args, **kwargs):
        serializer = super().get_serializer(*args, **kwargs)
        request = self.request

        # Usuário comum -> não pode mudar o status
        if not request.user.is_staff:
            serializer.fields["status"].read_only = True

        return serializer


    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializers_class = UserSerializer
    permission_classes = [IsAdminUser]