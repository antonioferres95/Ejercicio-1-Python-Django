from django.db import models
from django.db.models.deletion import CASCADE

class Client(models.Model):
    # BigInteger porque Integer no soporte la longitud del cuit
    cuit = models.BigIntegerField()
    name = models.CharField(max_length=50)
    clientCode = models.CharField(max_length=100)

    
class Invoice(models.Model):
    # Una factura pertenece a un cliente, y un cliente puede tener muchas facturas
    # Relación 1 a muchos
    client = models.ForeignKey(Client, on_delete=models.CASCADE,
                               null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    number = models.CharField(max_length=100)


class KindDetail(models.Model):
    name = models.CharField(max_length=100)





