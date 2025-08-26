from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Agenda

from rest_framework.serializers import ModelSerializer

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ['id', 'usuario', 'titulo', 'descricao', 'status' ,'data', 'hora', 'criado_em']
        read_only_fields = ['id', 'usuario', 'criado_em']

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'is_active']


