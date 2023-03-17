from django.shortcuts import render
from manejadorHistorias.logic.logic_Historias import getHistorias


def historiasList(request):
    context = {'listaHistorias': getHistorias()}
    return render(request, 'ManejadorHistorias/historias_list.html', context)

