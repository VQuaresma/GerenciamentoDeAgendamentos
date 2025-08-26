from django.db import models
from django.contrib.auth.models import User

class Agenda(models.Model):
    STATUS_CHOICES =[
        ("pendente", "PEN"),
        ("marcado", "MARC"),
        ("cancelado", "CANCEL")
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # quem criou
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pendente")
    data = models.DateField()
    hora = models.TimeField()
    criado_em = models.DateTimeField(auto_now_add=True)

    excluido = models.BooleanField(default=False)


    def __str__(self):
        status = "Cancelada" if self.cancelada else "Ativa"
        return f"{self.titulo} - {self.data} {self.hora}"
