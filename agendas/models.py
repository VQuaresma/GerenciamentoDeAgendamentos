from django.db import models
from django.contrib.auth.models import User

class Agenda(models.Model):
    STATUS_CHOICES =[
        ("pendente", "PEN"),
        ("marcado", "MARC"),
        ("cancelado", "CANCEL")
    ]

    titulo = models.CharField(max_length=200) # titulo do agendamento
    descricao = models.TextField(blank=True, null=True) # descrição do agendamento
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pendente") # status do agendamento
    #Data e hora do agendamento
    data = models.DateField() 
    hora = models.TimeField()

    #campos de auditoria
    excluido = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # quem criou

    """ 
    
    `modified_by` (último usuário que modificou)
    `modified_at` (data da última modificação)
    `deleted_by` (usuário que excluiu)
    `deleted_at` (data de exclusão)
    `is_deleted` (flag de exclusão lógica) """


    def __str__(self):
        status = "Cancelada" if self.cancelada else "Ativa"
        return f"{self.titulo} - {self.data} {self.hora}"
