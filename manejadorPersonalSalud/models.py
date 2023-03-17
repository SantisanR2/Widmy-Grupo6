from django.db import models

class PersonalSalud(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    fechaNacimiento = models.DateField()
    estaTurno = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
