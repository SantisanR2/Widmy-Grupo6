from django.urls import path

from . import views

urlpatterns = [
    path('personalSalud/', views.personalSaludList, name='personalSaludList'),
]