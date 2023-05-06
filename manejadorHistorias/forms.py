from django import forms
from .models import Historias

class HistoriasForm(forms.ModelForm):
    class Meta:
        model = Historias
        fields = [
            'descripcion',
        ]

        labels = {
            'descripcion' : 'Descripcion',
        }