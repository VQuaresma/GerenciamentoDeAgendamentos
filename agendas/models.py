from django.db import models
from django.contrib.auth.models import User

class Agenda(models.Model):
    STATUS_CHOICES =[
        ("pendente", "PEN"),
        ("marcado", "MARC"),
        ("cancelado", "CANCEL")
    ]

    titulo = models.CharField(max_length=200) 
    descricao = models.TextField(blank=True, null=True) 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pendente") 
    
    data = models.DateField() 
    hora = models.TimeField()

    #campos de auditoria
    excluido = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # quem criou

    modified_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="agendas_modificadas"
    ) 
    modified_at = models.DateTimeField(null=True, blank=True)  # data da última modificação

    deleted_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="agendas_excluidas"
    )  
    deleted_at = models.DateTimeField(null=True, blank=True)  # data da exclusão
    is_deleted = models.BooleanField(default=False)  # flag de exclusão lógica
    modified_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="agendas_modificadas"
    )  
    modified_at = models.DateTimeField(null=True, blank=True)  # data da última modificação

    deleted_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="agendas_excluidas"
    )  
    deleted_at = models.DateTimeField(null=True, blank=True)  
    is_deleted = models.BooleanField(default=False)  

    def __str__(self):
        status = "Cancelada" if self.cancelada else "Ativa"
        return f"{self.titulo} - {self.data} {self.hora}"
