from django import forms 
from .models import RegistroCliente

class RegistroClienteForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput)
    confirmar_contraseña = forms.CharField(widget=forms.PasswordInput)

    class Meta: 
        model = RegistroCliente
        fields = ['nombre', 'apellido', 'numero_telefono', 'correo']

        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('contraseña')
            confirm = cleaned_data.get('confirmar contraseña')
            if password and confirm and password != confirm: 
                raise forms.ValidationError('Las contraseñas no coinciden.')
            return cleaned_data