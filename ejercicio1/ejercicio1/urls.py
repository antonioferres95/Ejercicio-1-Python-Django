# Django
from django.contrib import admin
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Models
from invoices.views import clients, invoices, kinds_detail

router = DefaultRouter()
router.register(r'kinds_detail', kinds_detail.KindDetailViewSet, basename='kinds_detail')
router.register(r'clients', clients.ClientViewSet, basename='clients')

urlpatterns = [
    path('admin/', admin.site.urls),

    # Clientes, Tipos Detalle
    path('', include(router.urls)),

    # Facturas
    path('facturas/', invoices.index),
    path('facturas/alta_factura', invoices.altaFactura),
    path('facturas/baja_factura', invoices.bajaFactura),
    path('facturas/modifica_factura', invoices.modificaFactura),
]
