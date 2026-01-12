from django.db import models
from consultas.models import Consulta

class Prontuario(models.Model):
    consulta = models.OneToOneField(
        Consulta,
        on_delete=models.CASCADE,
        related_name='prontuario'
    )
    queixa_principal = models.TextField()
    evolucao = models.TextField()
    conduta = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
       return f"Prontuário - {self.consulta}"
