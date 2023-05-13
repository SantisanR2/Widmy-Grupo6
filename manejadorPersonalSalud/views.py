from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .logic.personalSalud_logic import getPersonalSalud
from .forms import PersonalSaludForm
from django.contrib import messages
from django.urls import reverse
from .logic.personalSalud_logic import createPersonalSalud
from encriptador.encriptador import generar_hash

def personalSaludList(request):
    personalSalud = getPersonalSalud()
    context = {'listaPersonal': personalSalud}
    return render(request, 'ManejadorPersonalSalud/personalSalud_list.html', context)

def personalSaludCreate(request):
    if request.method == 'POST':
        form = PersonalSaludForm(request.POST)

        if form.is_valid():
            hash = generar_hash(form.cleaned_data['nombre'])
            #hash = "hash_errado"
            print("Hash generado: " + hash)
            createPersonalSalud(form, hash)
            messages.add_message(request, messages.SUCCESS, 'Personal Salud Creado Correctamente')
            return HttpResponseRedirect(reverse('personalSaludCreate'))
        else:
            print(form.errors)
    else:
        form = PersonalSaludForm()

    context = {
        'form': form,
    }

    return render(request, 'ManejadorPersonalSalud/personalSalud_create.html', context)