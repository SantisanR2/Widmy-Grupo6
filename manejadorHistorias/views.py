from django.shortcuts import render
from manejadorHistorias.logic.logic_Historias import getHistorias
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from widmy.auth0backend import getRole
from .forms import HistoriasForm

@login_required
def historiasList(request):
    role = getRole(request)
    if (role == 'Administrador'):
        context = {'listaHistorias': getHistorias()}
        print(context)
        return render(request, 'ManejadorHistorias/historias_List.html', context)
    else:
        return HttpResponse("<h1>No tienes permitido ver las historias clínicas</h1><img src=""https://static.vecteezy.com/system/resources/previews/002/306/712/non_2x/warning-symbol-sign-vector.jpg"">")
    

