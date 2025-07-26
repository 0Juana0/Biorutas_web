from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('registro-cliente/', views.registro_cliente, name='registro_cliente'),
    path('reset-password/', views.reset_password, name='reset_password'),
    path('gracias/', views.gracias, name='gracias'),  # ← name='gracias' exacto
    path('login/', views.login_view, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('logout/', views.logout_view, name='logout'),
    path('paquetes/', views.paquetes, name='paquetes'),
    path('paquete-diamante/', views.paquete_diamante, name='paquete_diamante'),
    path('paquete-oro/',       views.crear_reserva, {'paquete_nombre': 'oro'},       name='paquete_oro'),
    path('paquete-diamante/',  views.crear_reserva, {'paquete_nombre': 'diamante'},  name='paquete_diamante'),
    path('paquete-platino/',   views.crear_reserva, {'paquete_nombre': 'platino'},   name='paquete_platino'),
    path('paquete-esmeralda/', views.crear_reserva, {'paquete_nombre': 'esmeralda'}, name='paquete_esmeralda'),
    path('paquete-zafiro/',    views.crear_reserva, {'paquete_nombre': 'zafiro'},    name='paquete_zafiro'),
    path('paquete-aventura/',  views.crear_reserva, {'paquete_nombre': 'aventura'},  name='paquete_aventura'),
    path('gracias-reserva/', views.gracias_reserva, name='gracias_reserva'),
    path('hoteles/', views.hoteles, name='hoteles'),
    path('vuelos/',   views.vuelos,  name='vuelos'),
]

