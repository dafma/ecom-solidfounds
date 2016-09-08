from django.shortcuts import render
from .forms import ArticuloForm, CategoriasForm, ProvedorForm
from ecomerce.shop.forms import ProductoForm
# Create your views here.


def inventario(request):
    return render(request, 'inventario.html')

def articulo(request):
    form = ArticuloForm()
    return render(request,'articulo.html', {'form':form} )

def lista_articulos(request):
    return render(request, )

def categorias(request):
    return render(request, 'categorias/categorias.html', {
        # 'form':form
    })

def categoria(request):
    form = ProductoForm()
    return render(request,'categorias/categoria.html', {'form':form})

def provedores(request):
    return render(request,'provedores/provedores.html' )

def provedor(request):
    form = ProvedorForm
    return render(request, 'provedores/provedor.html',{'form':form})