from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Paciente
from .forms import PacienteForm
from django.contrib.auth.decorators import login_required

@login_required
def paciente_list(request):
    pacientes = Paciente.objects.all().order_by('nome')
    return render(request, 'pacientes/index.html', {'pacientes': pacientes})


def paciente_create(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente cadastrado com sucesso.')
            return redirect('paciente_list')
    else:
        form = PacienteForm()

    return render(request, 'pacientes/form.html', {'form': form})


def paciente_update(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente atualizado com sucesso.')
            return redirect('paciente_list')
    else:
        form = PacienteForm(instance=paciente)

    return render(request, 'pacientes/form.html', {'form': form})


def paciente_delete(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)

    if request.method == 'POST':
        paciente.delete()
        messages.success(request, 'Paciente removido com sucesso.')
        return redirect('paciente_list')

    return render(request, 'pacientes/confirmar_exclusao.html', {'paciente': paciente})
