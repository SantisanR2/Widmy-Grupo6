from manejadorHistorias.models import Procedimientos


def getProcedimientos(self, idAdenda):
    queryset = Procedimientos.objects.filter(idAdenda=idAdenda)
    return (queryset)