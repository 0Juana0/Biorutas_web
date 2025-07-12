from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('registro-cliente/', views.registro_cliente, name='registro_cliente'),
    path('gracias/', views.gracias, name='gracias'),  # ← name='gracias' exacto
]