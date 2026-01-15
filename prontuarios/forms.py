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
            'queixa_principal': forms.Textarea(attrs={'rows': 3}),
            'evolucao': forms.Textarea(attrs={'rows': 4}),
            'conduta': forms.Textarea(attrs={'rows': 3}),
        }
