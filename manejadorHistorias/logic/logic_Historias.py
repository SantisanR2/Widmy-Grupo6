from manejadorHistorias.models import Historias

def getHistorias():
    queryset = Historias.objects.all()
    return (queryset)

def getHistoriaById(idHistoria):
    queryset = Historias.objects.filter(id=idHistoria)
    return (queryset)