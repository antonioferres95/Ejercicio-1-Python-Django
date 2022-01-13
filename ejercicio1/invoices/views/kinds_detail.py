# Django
from rest_framework import viewsets

# Models
from invoices.models.kinds_detail import KindDetail

# Serializers
from invoices.serializers.kinds_detail import KindDetailModelSerializer

class KindDetailViewSet(viewsets.ModelViewSet):
    """Kind Detail ViewSet."""

    queryset = KindDetail.objects.all()
    serializer_class = KindDetailModelSerializer