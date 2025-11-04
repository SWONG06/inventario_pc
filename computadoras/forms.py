from django import forms
from .models import Computadora, Proveedor

class ComputadoraForm(forms.ModelForm):
    class Meta:
        model = Computadora
        fields = '__all__'

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
