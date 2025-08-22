from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import HomeSerializer
from .serializers import serializers

class HomeViewSet(viewsets.ViewSet):
    def list(self, request):
        data = {"message": "Bem-vindo à homepage!"}
        serializer = HomeSerializer(data)
        return Response(serializer.data)