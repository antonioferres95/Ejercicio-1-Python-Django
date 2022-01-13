# Django
from rest_framework import serializers

# Models
from invoices.models.kinds_detail import KindDetail


class KindDetailModelSerializer(serializers.ModelSerializer):
    """Kind Detail Model Serializer."""

    class Meta:
        model = KindDetail
        fields = ['name']