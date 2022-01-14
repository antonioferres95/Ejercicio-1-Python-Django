# Django
from rest_framework import serializers

# Models
from invoices.models.clients import Client


class ClientModelSerializer(serializers.ModelSerializer):
    """Client Model Serializer."""

    class Meta:
        model = Client
        fields = ['cuit', 'name', 'clientCode']