from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from ecomerce.shop.models import Producto
from .cart import Cart
from .comparate import Comparar
from .forms import CartAddProductForm, CompararAddProductForm


# views cart
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Producto, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Producto, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
                                    initial={'quantity':item['quantity'],
                                             'update':True
                                             }
        )
    coupon_apply_form = CouponApplyForm()
    return render(request, 'cart/detail.html', {'cart':cart,
                                                'coupon_form': coupon_apply_form })

#views comparate
@require_POST
def ccart_add(request, product_id):
    comparar = Comparar(request)
    product = get_object_or_404(Producto, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        comparar.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:ccart_detail')

def ccart_remove(request, product_id):
    comparar = Comparar(request)
    product = get_object_or_404(Producto, id=product_id)
    comparar.remove(product)
    return redirect('cart:ccart_detail')

def ccart_detail(request):
    comparar = Comparar(request)
    for item in comparar:
        item['update_quantity_form'] = CompararAddProductForm(
                                    initial={'quantity':item['quantity'],
                                             'update':True
                                             }
        )
    coupon_apply_form = CouponApplyForm()
    return render(request, 'cart/comparar.html', {'comparar':comparar,
                                                'coupon_form': coupon_apply_form })