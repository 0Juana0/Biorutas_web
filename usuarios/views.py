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

def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)

            # 1) Si hay cliente en sesión, lo asignamos
            cliente_id = request.session.get('cliente_id')
            if cliente_id:
                reserva.cliente = RegistroCliente.objects.get(id=cliente_id)

            # 2) Guardamos la reserva sin cliente si no hay sesión
            reserva.paquete = 'Oro'
            total_base = 250000
            if reserva.extra_guia_bilingue:
                total_base += 20000
            if reserva.extra_souvenir:
                total_base += 10000
            if reserva.extra_seguro_viaje:
                total_base += 15000
            reserva.total_estimado = total_base
            reserva.save()

            messages.success(request, 'Reserva creada temporalmente sin cliente.')
            return redirect('usuarios:paquete_oro')
        else:
            messages.error(request, form.errors)
    else:
        form = ReservaForm()

    return render(request, 'usuarios/paquete_oro.html', {'form': form})