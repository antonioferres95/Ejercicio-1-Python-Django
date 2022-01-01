from django.db import models

class KindDetail(models.Model):
    
    name = models.CharField(max_length=100)