from django.contrib import admin
from django.urls import path
from invoices.views import clients, invoices, kinds_detail

urlpatterns = [
    path('admin/', admin.site.urls),

    # Clientes
    path('clientes/', clients.index),
    path('clientes/alta_cliente', clients.altaCliente),
    path('clientes/baja_cliente', clients.bajaCliente),
    path('clientes/modifica_cliente', clients.modificaCliente),

    # Tipos detalle
    path('tipos_detalle/', kinds_detail.index),
    path('tipos_detalle/alta_tipo_detalle', kinds_detail.altaTipoDetalle),
    path('tipos_detalle/baja_tipo_detalle', kinds_detail.bajaTipoDetalle),
    path('tipos_detalle/modifica_tipo_detalle', kinds_detail.modificaTipoDetalle),

    # Facturas
    path('facturas/', invoices.index),
    path('facturas/alta_factura', invoices.altaFactura),
    path('facturas/baja_factura', invoices.bajaFactura),
    path('facturas/modifica_factura', invoices.modificaFactura),
]
