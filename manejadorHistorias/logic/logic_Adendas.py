from manejadorHistorias.models import Adendas

def getAdendas(self, idHistoria):
    queryset = Adendas.objects.filter(idHistoria=idHistoria)
    return (queryset)
    