from django import forms
from .models import Pensamento

class PensamentoForm(forms.ModelForm):
    class Meta:
        model = Pensamento
        fields = ['tipo', 'texto']