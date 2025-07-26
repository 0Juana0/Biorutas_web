from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .forms import RegistroClienteForm, ReservaForm
from django.contrib.auth.hashers import check_password 
from .models import RegistroCliente, Paquete


def registro_cliente(request):
    if request.method == 'POST':
        form = RegistroClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.contraseña = make_password(form.cleaned_data['contraseña'])
            cliente.save()
            return redirect('usuarios:gracias')   # o solo 'gracias' si no usas namespace
    else:
        form = RegistroClienteForm()
    return render(request, 'usuarios/registro_cliente.html', {'form': form})

def gracias(request):
    return render(request, 'usuarios/gracias.html')

def login_view(request):
    # Si el usuario envió el formulario (botón "Entrar")
    if request.method == 'POST':
        correo = request.POST['correo']          # lo que escribió en el campo "correo"
        contraseña = request.POST['contraseña']  # lo que escribió en el campo "contraseña"

        try:
            # Buscamos al cliente con ese correo
            cliente = RegistroCliente.objects.get(correo=correo)

            # Verificamos que la contraseña coincida
            if check_password(contraseña, cliente.contraseña):
                # Guardamos su ID en la sesión (como una "etiqueta" en su navegador)
                request.session['cliente_id'] = cliente.id
                request.session['cliente_nombre'] = cliente.nombre
                # Redirigimos a la página de bienvenida
                return redirect('usuarios:gracias')
            else:
                error = "Contraseña incorrecta"
        except RegistroCliente.DoesNotExist:
            error = "No existe una cuenta con ese correo"

        # Si algo falló, volvemos a mostrar el formulario con el mensaje
        return render(request, 'usuarios/login.html', {'error': error})
    
     # Si llega por GET (solo quiere ver el formulario)
    return render(request, 'usuarios/login.html')

def inicio(request):
    # Si no tiene la etiqueta "cliente_id" lo devolvemos al login
    if not request.session.get('cliente_id'):
        return redirect('usuarios:login')

    nombre = request.session.get('cliente_nombre')
    return render(request, 'usuarios/inicio.html', {'nombre': nombre})

def logout_view(request):
    request.session.flush()   # borra TODA la sesión
    return redirect('usuarios:login')

def paquetes(request):
    #Verificar que el usuario esté logueado
    #cliente_id = request.session.get('cliente_id')
    #if not cliente_id:
        #return redirect('usuarios:login')
    
    #Obtener las reservas del cliente 
    #paquetes = Paquete.objects.filter(usuario_id=cliente_id)
    return render(request,'usuarios/paquetes.html', {'paquetes':paquetes})

from django.shortcuts import render

def paquete_diamante(request):
    return render(request, 'usuarios/paquete_diamante.html')

#def paquete_oro(request):
 #   return render(request, 'usuarios/paquete_oro.html')

def paquete_platino(request):
    return render(request, 'usuarios/paquete_platino.html')

def paquete_esmeralda(request):
    return render(request, 'usuarios/paquete_esmeralda.html')

def paquete_zafiro(request):
    return render(request, 'usuarios/paquete_zafiro.html')

def paquete_aventura(request):
    return render(request, 'usuarios/paquete_aventura.html')

# Precios base (lo puedes mover a un modelo o settings más adelante)
PRECIOS_BASE = {
    'oro':       250000,
    'diamante':  350000,
    'platino':   400000,
    'esmeralda': 200000,
    'zafiro':    220000,
    'aventura':  180000,
}

def crear_reserva(request, paquete_nombre):
    paquete_nombre = paquete_nombre.lower()
    if paquete_nombre not in PRECIOS_BASE:
        messages.error(request, 'Paquete no válido.')
        return redirect('inicio')

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)

            # Asignar el paquete
            reserva.paquete = paquete_nombre.capitalize()

            # Calcular total
            total = PRECIOS_BASE[paquete_nombre]
            if reserva.extra_guia_bilingue:
                total += 20000
            if reserva.extra_souvenir:
                total += 10000
            if reserva.extra_seguro_viaje:
                total += 15000
            reserva.total_estimado = total

            # Cliente (opcional por ahora)
            cliente_id = request.session.get('cliente_id')
            if cliente_id:
                from .models import RegistroCliente
                reserva.cliente = RegistroCliente.objects.get(id=cliente_id)

            reserva.save()
            messages.success(request, f'¡Reserva del paquete {reserva.paquete} confirmada!')
            return redirect('usuarios:gracias_reserva')
    else:
        form = ReservaForm()

    context = {
        'form': form,
        'paquete_nombre': paquete_nombre,
        'precio_base': PRECIOS_BASE[paquete_nombre],
    }
    template = f'usuarios/paquete_{paquete_nombre}.html'
    return render(request, template, context)

# usuarios/views.py
from django.shortcuts import render

def gracias_reserva(request):
    """
    Muestra la página de confirmación de reserva.
    """
    return render(request, 'usuarios/gracias_reserva.html')

def hoteles(request):
    return render(request, 'usuarios/hoteles.html')

def vuelos(request):
    return render(request, 'usuarios/vuelos.html')