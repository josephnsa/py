from django.db import models
from .room_type import RoomType
from .room_status import RoomStatus
from .bed_type import BedType


class RoomCategory(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nombre de la categoría")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")

    class Meta:
        verbose_name = "Categoría de Cuarto"
        verbose_name_plural = "Categorías de Cuartos"

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.CharField(max_length=10, unique=True, verbose_name="Número")
    floor = models.IntegerField(verbose_name="Piso")
    category = models.ForeignKey(RoomCategory, on_delete=models.SET_NULL, null=True, verbose_name="Categoría")
    type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True, verbose_name="Tipo de Cuarto")
    status = models.ForeignKey(RoomStatus, on_delete=models.SET_NULL, null=True, verbose_name="Estado del Cuarto")
    bed_type = models.ForeignKey(BedType, on_delete=models.SET_NULL, null=True, verbose_name="Tipo de Cama")

    capacity = models.PositiveIntegerField(default=1, verbose_name="Capacidad")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio por noche")
    available = models.BooleanField(default=True, verbose_name="Disponible")
    image = models.ImageField(upload_to='rooms/', null=True, blank=True, verbose_name="Imagen del cuarto")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Cuarto"
        verbose_name_plural = "Cuartos"
        ordering = ['floor', 'number']

    def __str__(self):
        return f"Cuarto #{self.number} - Piso {self.floor}"
