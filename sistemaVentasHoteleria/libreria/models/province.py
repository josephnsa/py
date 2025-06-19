# libreria/models/province.py
from django.db import models
from .region import Region

class Province(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
