from django import forms
from matricula.models import *

class BoletimForm(forms.ModelForm):
    
    class Meta:
        model = DadosPessoais
        fields = '__all__'
        widgets = {
            'data_nascimento': forms.DateTimeInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Selecione a data', 'type': 'date'})
        }