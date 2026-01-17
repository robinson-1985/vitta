from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Consulta
from .forms import ConsultaForm
from datetime import date, datetime
from django.utils import timezone

def consulta_list(request):
    consultas = Consulta.objects.all().order_by('-data', '-hora')
    return render(
        request,
        'consultas/consulta_list.html',
        {'consultas': consultas}
    )


def consulta_create(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consulta agendada com sucesso.')
            return redirect('consulta_list')
    else:
        form = ConsultaForm()

    return render(
        request, 
        'consultas/consulta_form.html', 
        {'form': form}
    )   


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

    return render(
        request, 
        'consultas/consulta_form.html', 
        {'form': form}
    )


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


def consulta_agenda(request):
    data_selecionada = request.GET.get('data')
    
    if data_selecionada:
        consultas = Consulta.objects.filter(
            data__date=data_selecionada
        ).order_by('hora')
    else:
        consultas = Consulta.objects.filter(
            data__date=timezone.localdate()
        ).order_by('hora')
        
    return render(
        request, 
        'consultas/consulta_agenda.html', 
        {    
            'consultas': consultas, 
            'data_selecionada': data_selecionada
         }
    )
