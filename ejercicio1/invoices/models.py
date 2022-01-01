from django.db import models
from django.db.models.deletion import CASCADE
from clients.models import Client

class Invoice(models.Model):
    
    # Una factura pertenece a un cliente, y un cliente puede tener muchas facturas
    # Relación 1 a muchos
    client = models.ForeignKey(Client, on_delete=models.CASCADE,
                                null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    number = models.CharField(max_length=100)