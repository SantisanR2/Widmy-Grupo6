from ..models import PersonalSalud

#Devuelve todo el personal de salud
def getPersonalSalud():
    queryset = PersonalSalud.objects.all()
    return (queryset)

#Devuelve el personal de salud con el id dado
def getPersonalSaludById(id):
    return PersonalSalud.objects.get(id=id)

#Crea el personal de salud con los datos dados
def createPersonalSalud(nombre, especialidad, telefono, correo, direccion, fechaNacimiento, estaTurno):
    personalSalud = PersonalSalud(nombre=nombre, especialidad=especialidad, telefono=telefono, correo=correo, direccion=direccion, fechaNacimiento=fechaNacimiento, estaTurno=estaTurno)
    personalSalud.save()
    return personalSalud

#Actualiza el personal de salud con el id dado
def updatePersonalSalud(id, nombre, especialidad, telefono, correo, direccion, fechaNacimiento, estaTurno):
    personalSalud = PersonalSalud.objects.get(id=id)
    personalSalud.nombre = nombre
    personalSalud.especialidad = especialidad
    personalSalud.telefono = telefono
    personalSalud.correo = correo
    personalSalud.direccion = direccion
    personalSalud.fechaNacimiento = fechaNacimiento
    personalSalud.estaTurno = estaTurno
    personalSalud.save()
    return personalSalud

#Elimina el personal de salud con el id dado
def deletePersonalSalud(id):
    personalSalud = PersonalSalud.objects.get(id=id)
    personalSalud.delete()

#Devuelve el personal de salud que esta en turno
def getPersonalSaludEnTurno():
    return PersonalSalud.objects.filter(estaTurno=True)