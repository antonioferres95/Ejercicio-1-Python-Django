from django.contrib import admin

from django.urls import path

from clients import views as clients_view
from kind_details import views as kind_details_view
from invoices import views as invoices_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # Módulo clientes
    path('clientes/', clients_view.index),
    path('clientes/alta_cliente', clients_view.altaCliente),
    path('clientes/baja_cliente', clients_view.bajaCliente),
    path('clientes/modifica_cliente', clients_view.modificaCliente),

    # Módulo tipos detalle
    path('tipos_detalle/', kind_details_view.index),
    path('tipos_detalle/alta_tipo_detalle', kind_details_view.altaTipoDetalle),
    path('tipos_detalle/baja_tipo_detalle', kind_details_view.bajaTipoDetalle),
    path('tipos_detalle/modifica_tipo_detalle', kind_details_view.modificaTipoDetalle),

    # Módulo facturas
    path('facturas/', invoices_view.index),
    path('facturas/alta_factura', invoices_view.altaFactura),
    path('facturas/baja_factura', invoices_view.bajaFactura),
    path('facturas/modifica_factura', invoices_view.modificaFactura),
]
