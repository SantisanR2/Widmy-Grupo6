
from manejadorHistorias.models import ConsultasMedicas

def getConsultasMedicas(self, idAdenda):
    queryset = ConsultasMedicas.objects.filter(idAdenda=idAdenda)
    return (queryset)
