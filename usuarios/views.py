from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import RegistroClienteForm

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