from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('registro-cliente/', views.registro_cliente, name='registro_cliente'),
    path('gracias/', views.gracias, name='gracias'),  # ← name='gracias' exacto
    path('login/', views.login_view, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('logout/', views.logout_view, name='logout'),
    path('paquetes/', views.paquetes, name='paquetes'),
    path('paquete-diamante/', views.paquete_diamante, name='paquete_diamante'),
    #path('paquete-oro/', views.paquete_oro, name='paquete_oro'),
    path('paquete-oro/', views.crear_reserva, name='paquete_oro'),
    path('paquete-platino/', views.paquete_platino, name='paquete_platino'),
    path('paquete-esmeralda/', views.paquete_esmeralda, name='paquete_esmeralda'),
    path('paquete-zafiro/', views.paquete_zafiro, name='paquete_zafiro'),
    path('paquete-aventura/', views.paquete_aventura, name='paquete_aventura'),
]

