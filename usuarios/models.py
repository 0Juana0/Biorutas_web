from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=15, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username


class PaqueteViaje(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('cancelado', 'Cancelado'),
    ]
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    paquete = models.ForeignKey(PaqueteViaje, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

    def __str__(self):
        return f"{self.usuario.username} - {self.paquete.nombre}"