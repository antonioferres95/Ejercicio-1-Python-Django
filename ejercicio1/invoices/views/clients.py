# Django
from rest_framework import viewsets

# Models
from invoices.models.clients import Client

# Serializers
from invoices.serializers.clients import ClientModelSerializer


class ClientViewSet(viewsets.ModelViewSet):
    """Client ViewSet."""

    queryset = Client.objects.all()
    serializer_class = ClientModelSerializer