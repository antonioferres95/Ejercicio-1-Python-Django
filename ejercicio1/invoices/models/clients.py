from django.db import models


class Client(models.Model):
    """Client model."""

    cuit = models.BigIntegerField()
    # BigInteger porque Integer no soporte la longitud del cuit
    name = models.CharField(max_length=50)
    clientCode = models.CharField(max_length=100)


    def __str__(self):
        """Retorna el nombre y cuit de la persona."""
        return ("{} con cuit {}.".format(self.name, self.cuit))


    class Meta:

        db_table = 'client'