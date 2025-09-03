from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Agenda
from rest_framework.serializers import ModelSerializer

class AgendaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Agenda
        fields = [
            'id', 
            'titulo', 
            'descricao', 
            'status',
            'data', 
            'hora',
            'criado_por',
            'criado_em',
            'atualizado_por',
            'atualizado_em',
            'is_deleted', 
            'deleted_by', 
            'deleted_at'
        ]
        read_only_fields = [
            'id', 
            'criado_por', 
            'criado_em', 
            'atualizado_por', 
            'atualizado_em',
            'is_deleted', 
            'deleted_by', 
            'deleted_at'
        ]

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'is_active']