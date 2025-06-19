# libreria/models/document_type.py

from django.db import models

class DocumentType(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nombre del tipo de documento")
    abbreviation = models.CharField(max_length=10, unique=True, verbose_name="Abreviatura (DNI, RUC, etc.)")

    def __str__(self):
        return f"{self.abbreviation} - {self.name}"

    class Meta:
        verbose_name = "Tipo de Documento"
        verbose_name_plural = "Tipos de Documentos"
        ordering = ['name']
