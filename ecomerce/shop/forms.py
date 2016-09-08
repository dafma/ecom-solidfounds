from .models import Producto
from django import forms

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['categoria', 'nombre', 'slug', 'imagen', 'imagen2', 'imagen3', 'descripcion', 'precio', 'stock',
                  'disponible',]