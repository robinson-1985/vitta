from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from .forms import PacienteForm

def index(request):
    pacientes = Paciente.objects.all()
    return render(
        request, 
        'pacientes/index.html',
        {'pacientes': pacientes}
    )
    
    
def criar(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pacientes_index')
    else:
        form = PacienteForm()
        
    return render(request, 'pacientes/form.html', {'form': form})


def editar(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('pacientes_index')
    else:
        form = PacienteForm(instance=paciente)
        
    return render(request, 'pacientes/form.html', {'form': form})


def deletar(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    
    if request.method == 'POST':
        paciente.delete()
        return redirect('pacientes_index')

    return render(request, 'pacientes/confirmar_exclusao.html', {'paciente': paciente})
