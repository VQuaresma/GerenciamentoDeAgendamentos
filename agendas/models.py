from django.db import models
from django.contrib.auth.models import User

class Agenda(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # quem criou
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    data = models.DateField()
    hora = models.TimeField()
    cancelada = models.BooleanField(default=False)  # novo campo para cancelamento
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        status = "Cancelada" if self.cancelada else "Ativa"
        return f"{self.titulo} - {self.data} {self.hora}"
