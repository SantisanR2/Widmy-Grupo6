from django.urls import path
from . import views

urlpatterns = [
    path('historias/', views.historiasList, name='historiasList'),
]
