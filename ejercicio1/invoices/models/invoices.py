from django.db import models
from django.db.models.deletion import CASCADE
from invoices.models.clients import Client


class Invoice(models.Model):
    """Invoice model."""

    client = models.ForeignKey(Client, on_delete=models.CASCADE,
                               null=False, blank=False)
    # Una factura pertenece a un cliente, y un cliente puede tener muchas facturas
    # Relación 1 a muchos
    date = models.DateTimeField(auto_now_add=True)
    number = models.CharField(max_length=100)


    def __str__(self):
        """Retorna el id de la factura y el nombre del cliente."""
        return ("{} del cliente {}.".format(self.id, self.client.name))


    class Meta:

        db_table = 'invoice'