from django.contrib.auth.models import AbstractUser
from django.db import models
from .region import Region
from .district import District

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50, verbose_name="Nombres")
    last_name = models.CharField(max_length=50, verbose_name="Apellidos")
    dni = models.CharField(max_length=20, unique=True, verbose_name="DNI")
    email = models.EmailField(unique=True, verbose_name="Correo electrónico")
    phone = models.CharField(max_length=15, verbose_name="Teléfono")
    address = models.CharField(max_length=255, verbose_name="Dirección")
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    email_confirmed = models.BooleanField(default=False)
    accepted_terms = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email', 'dni', 'phone', 'first_name', 'last_name', 'address']

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"
