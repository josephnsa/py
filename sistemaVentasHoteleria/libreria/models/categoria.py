from django.db import models

class CategoriaCuarto(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name="Nombre de la categoría")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    def __str__(self):
        return self.nombre
