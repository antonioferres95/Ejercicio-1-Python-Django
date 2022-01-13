# Django
from django.contrib import admin
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Models
from invoices.views import clients, invoices, kinds_detail

router = DefaultRouter()
router.register(r'kinds_detail', kinds_detail.KindDetailViewSet, basename='kinds_detail')

urlpatterns = [
    path('admin/', admin.site.urls),

    # Clientes
    path('clientes/', clients.index),
    path('clientes/alta_cliente', clients.altaCliente),
    path('clientes/baja_cliente', clients.bajaCliente),
    path('clientes/modifica_cliente', clients.modificaCliente),

    # Tipos detalle
    path('', include(router.urls)),

    # Facturas
    path('facturas/', invoices.index),
    path('facturas/alta_factura', invoices.altaFactura),
    path('facturas/baja_factura', invoices.bajaFactura),
    path('facturas/modifica_factura', invoices.modificaFactura),
]
