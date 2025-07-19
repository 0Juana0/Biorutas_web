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
        confirm = cleaned_data.get('confirmar_contraseña')
        if password and confirm and password != confirm: 
            self.add_error('confirmar_contraseña', 'Las contraseñas no coinciden.')
        
        return cleaned_data