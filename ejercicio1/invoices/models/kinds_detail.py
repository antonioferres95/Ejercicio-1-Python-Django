from django.db import models


class KindDetail(models.Model):
    """Kind Detail model."""
    name = models.CharField(max_length=100)


    def __str__(self):
        """Retorna el id y name del tipo detalle."""
        return ("{} con nombre {}.".format(self.id, self.name))


    class Meta:

        db_table = 'kind_detail'