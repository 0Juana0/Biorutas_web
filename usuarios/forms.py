from django import forms 
from .models import RegistroCliente
from django.core.exceptions import ValidationError

class RegistroClienteForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput)
    confirmar_contraseña = forms.CharField(widget=forms.PasswordInput)

    class Meta: 
        model = RegistroCliente
        fields = ['nombre', 'apellido', 'numero_telefono', 'correo']

    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if RegistroCliente.objects.filter(correo=correo).exists():
            raise ValidationError('Este correo ya está registrado.')
        return correo


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('contraseña')
        confirm = cleaned_data.get('confirmar_contraseña')
        if password and confirm and password != confirm: 
            self.add_error('confirmar_contraseña', 'Las contraseñas no coinciden.')
        return cleaned_data