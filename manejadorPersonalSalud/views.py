from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .logic.personalSalud_logic import getPersonalSalud

def personalSaludList(request):
    personalSalud = getPersonalSalud()
    context = {'listaPersonal': personalSalud}
    return render(request, 'ManejadorPersonalSalud/personalSalud_list.html', context)

