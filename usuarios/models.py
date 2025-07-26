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

    def __str__(self):
        return f"{self.usuario.username} - {self.paquete.nombre}"
    
class RegistroCliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100) 
    numero_telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128) 
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Paquete(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('cancelado', 'Cancelado'),
    ]
    usuario = models.ForeignKey(RegistroCliente, on_delete=models.CASCADE)
    paquete = models.ForeignKey(PaqueteViaje, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')


def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Reserva(models.Model):
    cliente = models.ForeignKey(
        RegistroCliente,
        on_delete=models.CASCADE,
        null=True,       # ← permite NULL
        blank=True       # ← permite dejar vacío en formularios/admin
    )
    paquete = models.CharField(max_length=100)  # Identificador del paquete
    fecha_tour = models.DateField()
    cantidad_personas = models.IntegerField()
    extra_guia_bilingue = models.BooleanField(default=False)
    extra_souvenir = models.BooleanField(default=False)
    extra_seguro_viaje = models.BooleanField(default=False)
    total_estimado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Reserva de {self.cliente.nombre} {self.cliente.apellido} para {self.fecha_tour}"