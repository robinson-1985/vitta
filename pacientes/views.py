from django.shortcuts import render
from .models import Paciente

def index(request):
    pacientes = Paciente.objects.all()
    return render(
        request, 
        'pacientes/index.html',
        {'pacientes': pacientes}
    )
