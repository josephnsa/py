from django.db import models
from .document_type import DocumentType  # Asegúrate de tener este import correcto

class Staff(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Nombre completo")
    role = models.CharField(max_length=50, verbose_name="Cargo o función")
    
    document_type = models.ForeignKey(DocumentType, on_delete=models.PROTECT, verbose_name="Tipo de documento")
    document_number = models.CharField(max_length=20, verbose_name="Número de documento")
    
    email = models.EmailField(verbose_name="Correo electrónico")
    phone = models.CharField(max_length=15, verbose_name="Teléfono")
    
    active = models.BooleanField(default=True, verbose_name="Activo")

    def __str__(self):
        return f"{self.full_name} - {self.role}"

    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "Personal"
        ordering = ['full_name']
