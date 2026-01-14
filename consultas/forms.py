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


    def clean(self):
        cleaned_data = super().clean()
        data = cleaned_data.get('data')
        hora = cleaned_data.get('hora')
        profissional = cleaned_data.get('profissional')

        if data and hora and profissional:
            conflito = Consulta.objects.filter(
                data=data,
                hora=hora,
                profissional=profissional,
                status__in=['AGENDADA', 'REALIZADA']
            )
            
            if self.instance.pk:
                conflito = conflito.exclude(pk=self.instance.pk)

            if conflito.exists():
                raise forms.ValidationError(
                    "Já existe uma consulta agendada para esta data e hora."
                )

        return cleaned_data
