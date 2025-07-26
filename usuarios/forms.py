from django import forms 
from .models import RegistroCliente, Reserva
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
    
class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['fecha_tour', 'cantidad_personas', 'extra_guia_bilingue', 'extra_souvenir', 'extra_seguro_viaje']
        widgets = {
            'fecha_tour': forms.DateInput(attrs={'type': 'date'}),
            'cantidad_personas': forms.NumberInput(attrs={'type': 'number'}),
            'extra_guia_bilingue': forms.CheckboxInput(),
            'extra_souvenir': forms.CheckboxInput(),
            'extra_seguro_viaje': forms.CheckboxInput(),
        }