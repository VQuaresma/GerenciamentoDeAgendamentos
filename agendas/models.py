from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

# Modelo Agenda
class Agenda(BaseModel):
    STATUS_CHOICES = [
        ("pendente", "PEN"),
        ("marcado", "MARC"),
        ("cancelado", "CANCEL")
    ]

    titulo = models.CharField(max_length=200) 
    descricao = models.TextField(blank=True, null=True) 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pendente") 
    
    data = models.DateField() 
    hora = models.TimeField()
    
    # Campos de auditoria para usuários
    criado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="agendas_criadas"
    )
    atualizado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="agendas_atualizadas"
    )

    # Campos de soft delete
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="agendas_deletadas"
    )
    
    def __str__(self):
        return f"{self.titulo} - {self.data} {self.hora} ({self.get_status_display()})"