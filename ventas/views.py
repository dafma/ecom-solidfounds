
# Create your views here.
from django.shortcuts import render
from inventario.models import Articulo

# Create your views here.


def carrito(request):
    articulos = Articulo.objects.all()
    return render(request,'ventas_carrito.html', {"articulos":articulos})

def calendario_eventos(request):
    return render(request, 'calendario-eventos.html')