# libreria/models/customer.py

from django.db import models
from .document_type import DocumentType

class Customer(models.Model):
    document_type = models.ForeignKey(DocumentType, on_delete=models.PROTECT, verbose_name="Tipo de documento")
    document_number = models.CharField(max_length=20, null=True, blank=True, verbose_name="Numero documento")
    full_name = models.CharField(max_length=100, verbose_name="Nombre completo")
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} ({self.document_type.abbreviation}: {self.document_number})"
