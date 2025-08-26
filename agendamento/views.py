from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import HomeSerializer
from drf_yasg.utils import swagger_auto_schema



class HomeViewSet(viewsets.ViewSet):

    @swagger_auto_schema(
        operation_description="Retorna uma mensagens de boas vindas da API",
        responses={200: HomeSerializer()}
    )
    def list(self, request):
        data = {"message": "Bem-vindo à homepage!"}
        serializer = HomeSerializer(data)
        return Response(serializer.data)
    
