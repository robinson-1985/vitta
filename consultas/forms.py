from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'hora': forms.TimeInput(
                attrs={'type': 'time'}
            ),
        }
