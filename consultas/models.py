from django.db import models
from pacientes.models import Paciente

class Consulta(models.Model):
    STATUS_CHOICES = [
      ('AGENDADA', 'Agendada'),
      ('REALIZADA', 'Realizada'),
      ('CANCELADA', 'Cancelada'),
    ]
    
    paciente = models.ForeignKey(
        Paciente, 
        on_delete=models.CASCADE,
        related_name='consultas'
        )
    
    data = models.DateTimeField()
    hora = models.TimeField()
    
    profissional = models.CharField(max_length=100)
    
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='AGENDADA'
        )
    
    observacoes = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.paciente.nome} - {self.data} {self.hora}"
