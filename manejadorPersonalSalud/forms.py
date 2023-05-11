from django import forms
from .models import PersonalSalud

class PersonalSaludForm(forms.ModelForm):
    class Meta:
        model = PersonalSalud
        fields = [
            'nombre',
            'especialidad',
            'telefono',
            'correo',
            'direccion',
            'fechaNacimiento',
            'estaTurno',
        ]

        labels = {
            'nombre': 'Nombre',
            'especialidad': 'Especialidad',
            'telefono': 'Telefono',
            'correo': 'Correo',
            'direccion': 'Direccion',
            'fechaNacimiento': 'Fecha de Nacimiento',
            'estaTurno': 'Esta en Turno',
        }