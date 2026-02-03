from django.shortcuts import render, get_object_or_404, redirect
from consultas.models import Consulta
from .models import Prontuario
from .forms import ProntuarioForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def prontuarios_home(request):
    return HttpResponse("Prontuários: use /prontuarios/consulta/<id>/")


def criar_prontuario(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    
    prontuario, created = Prontuario.objects.get_or_create(
        consulta=consulta
    )
    
    if request.method == 'POST':
        form = ProntuarioForm(request.POST, instance=prontuario)
        if form.is_valid():
            form.save()
            return redirect('consulta_list')
    else:
        form = ProntuarioForm(instance=prontuario)
    
    return render(
        request, 
        'prontuarios/prontuario_form.html', 
        {
            'form': form, 
            'consulta': consulta,
            'created': created
            }
        
        )
