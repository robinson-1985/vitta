from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Consulta
from .forms import ConsultaForm

def consulta_list(request):
    consultas = Consulta.objects.select_related().order_by('data', 'hora')
    return render(request, 'consultas/list.html', {'consultas': consultas})


def consulta_create(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consulta agendada com sucesso.')
            return redirect('consulta_list')
    else:
        form = ConsultaForm()

    return render(request, 'consultas/form.html', {'form': form})


def consulta_update(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)

    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consulta atualizada com sucesso.')
            return redirect('consulta_list')
    else:
        form = ConsultaForm(instance=consulta)

    return render(request, 'consultas/form.html', {'form': form})


def consulta_delete(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)

    if request.method == 'POST':
        consulta.delete()
        messages.success(request, 'Consulta removida com sucesso.')
        return redirect('consulta_list')

    return render(
        request, 
        'consultas/confirm_delete.html', 
        {'consulta': consulta}
        )
