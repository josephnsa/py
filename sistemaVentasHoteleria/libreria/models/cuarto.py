from django.db import models
from .categoria import CategoriaCuarto

class Cuarto(models.Model):
    numero = models.CharField(max_length=10, unique=True, verbose_name="Número del cuarto")
    piso = models.IntegerField(verbose_name="Piso")
    categoria = models.ForeignKey(CategoriaCuarto, on_delete=models.SET_NULL, null=True, verbose_name="Categoría")
    capacidad = models.PositiveIntegerField(default=1, verbose_name="Capacidad de personas")
    
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción del cuarto")
    servicios = models.TextField(
        blank=True,
        null=True,
        verbose_name="Servicios incluidos (separados por comas)",
        help_text="Ej: WiFi, TV, Aire acondicionado"
    )

    imagen = models.ImageField(
        upload_to='imagenes_cuartos/',
        blank=True,
        null=True,
        verbose_name="Imagen del cuarto"
    )

    precio_por_noche = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Precio por noche"
    )
    
    disponible = models.BooleanField(default=True, verbose_name="Disponible")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Cuarto"
        verbose_name_plural = "Cuartos"
        ordering = ['piso', 'numero']

    def __str__(self):
        return f"Cuarto {self.numero} - Piso {self.piso} ({'Disponible' if self.disponible else 'Ocupado'})"
