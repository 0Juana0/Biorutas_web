from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('registro-cliente/', views.registro_cliente, name='registro_cliente'),
    path('gracias/', views.gracias, name='gracias'),  # ← name='gracias' exacto
    path('login/', views.login_view, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('logout/', views.logout_view, name='logout'),
]

