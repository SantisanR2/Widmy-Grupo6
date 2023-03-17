from django.db import models

class Historias(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=200)

class Adendas(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=200)
    id_historia = models.ForeignKey('Historias', models.DO_NOTHING, db_column='id_historia')


class ConsultasMedicas(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=200)
    id_adenda = models.ForeignKey('Adendas', models.DO_NOTHING, db_column='id_adenda')

class Procedimientos(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=200)
    id_adenda = models.ForeignKey('Adendas', models.DO_NOTHING, db_column='id_adenda')