from manejadorHistorias.models import Historias

def getHistorias():
    queryset = Historias.objects.all()
    return (queryset)

def getHistoriaById(idHistoria):
    queryset = Historias.objects.filter(id=idHistoria)
    return (queryset)

def updateHistoria(idHistoria, idPaciente, idPersonalSalud, fecha, sintomas, diagnostico, tratamiento):
    historia = Historias.objects.get(id=idHistoria)
    historia.idPaciente = idPaciente
    historia.idPersonalSalud = idPersonalSalud
    historia.fecha = fecha
    historia.sintomas = sintomas
    historia.diagnostico = diagnostico
    historia.tratamiento = tratamiento
    historia.save()
    return historia