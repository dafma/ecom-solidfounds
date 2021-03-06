"""EcomSolidfounds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from ecomerce.shop import views
urlpatterns = [
        url(r'^admin/', admin.site.urls),
    url(r'^cpanel/', include('reportes.urls')),
    url(r'^cpanel_inventario/', include('inventario.urls', namespace='inventario')),
    url(r'^cpanel_ventas/', include('ventas.urls', namespace='ventas')),
    url(r'^cpanel_clientes/', include('clientes.urls', namespace='clientes')),
    url(r'^cpanel_gastos/', include('gastos.urls', namespace='gastos')),
    #ecomerce
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^cart/', include('ecomerce.cart.urls', namespace='cart')),
    url(r'^', include('ecomerce.shop.urls', namespace='shop')),
    url(r'^ordern/', include('ecomerce.orders.urls', namespace='orders')),
    url(r'^payment/', include('payment.urls', namespace='payment')),
    #api
    url(r'api/', include('api.urls')),
    #search
    url(r'^s/',views.search_productt, name='search_productt'),
]
