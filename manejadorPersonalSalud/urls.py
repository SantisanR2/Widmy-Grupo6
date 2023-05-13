from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('personalSalud/', views.personalSaludList, name='personalSaludList'),
    path('personalSaludCreate/', csrf_exempt(views.personalSaludCreate), name='personalSaludCreate'),
]