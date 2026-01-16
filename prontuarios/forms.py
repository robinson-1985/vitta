from django import forms
from .models import Prontuario

class ProntuarioForm(forms.ModelForm):
    class Meta:
        model = Prontuario
        fields = [
            'queixa_principal',
            'evolucao',
            'conduta',
        ]
        widgets = {
            'queixa_principal': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Descreva a queixa principal do paciente.'
                }),
            'evolucao': forms.Textarea(attrs={
                'rows': 6,
                'placeholder': 'Evolução clínica.'}),
            'conduta': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Conduta adotada.'
                }),
        }
        labels = {
            'queixa_principal': 'Queixa Principal',
            'evolucao': 'Evolução',
            'conduta': 'Conduta',
        }
