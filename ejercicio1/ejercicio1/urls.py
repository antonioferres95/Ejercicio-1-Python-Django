from django.contrib import admin
from django.urls import path
from invoices import views as invoices_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # Clientes
    path('clientes/', invoices_view.index),
    path('clientes/alta_cliente', invoices_view.altaCliente),
    path('clientes/baja_cliente', invoices_view.bajaCliente),
    path('clientes/modifica_cliente', invoices_view.modificaCliente),

    # Tipos detalle
    path('tipos_detalle/', invoices_view.index),
    path('tipos_detalle/alta_tipo_detalle', invoices_view.altaTipoDetalle),
    path('tipos_detalle/baja_tipo_detalle', invoices_view.bajaTipoDetalle),
    path('tipos_detalle/modifica_tipo_detalle', invoices_view.modificaTipoDetalle),

    # Facturas
    path('facturas/', invoices_view.index),
    path('facturas/alta_factura', invoices_view.altaFactura),
    path('facturas/baja_factura', invoices_view.bajaFactura),
    path('facturas/modifica_factura', invoices_view.modificaFactura),
]
