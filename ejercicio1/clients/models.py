from django.db import models

class Client(models.Model):
    
    # BigInteger porque Integer no soporte la longitud del cuit
    cuit = models.BigIntegerField()
    name = models.CharField(max_length=50)
    clientCode = models.CharField(max_length=100)
