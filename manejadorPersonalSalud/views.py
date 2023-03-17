from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .logic.personalSalud_logic import getPersonalSaludList

def personalSaludList(request):
    personalSalud = getPersonalSaludList()
    context = {'personalSalud': personalSalud}
    return render(request, 'ManejadorPersonalSalud/personalSalud_list.html', context)

