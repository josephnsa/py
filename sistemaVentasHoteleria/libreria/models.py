from django.db import models
from django.utils import timezone
import uuid 
# Create your models here.

from django.db import models

class CategoriaCuarto(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name="Nombre de la categoría")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    def _str_(self):
        return self.nombre


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

    def _str_(self):
        return f"Cuarto {self.numero} - Piso {self.piso} ({'Disponible' if self.disponible else 'Ocupado'})"
ESTADO_RESERVA_CHOICES = [
    ('reservado', 'Reservado'),
    ('ocupado', 'Ocupado'),
    ('cancelado', 'Cancelado'),
    ('finalizado', 'Finalizado'),
]


class ReservaCuarto(models.Model):
    codigo_reserva = models.CharField(
        max_length=12,
        unique=True,
        editable=False,
        verbose_name="Código de Reserva"
    )
    
    nombre_cliente = models.CharField(max_length=100, verbose_name="Nombre del cliente")
    documento_cliente = models.CharField(max_length=20, verbose_name="Documento del cliente")
    correo_cliente = models.EmailField(blank=True, null=True, verbose_name="Correo del cliente")
    telefono_cliente = models.CharField(max_length=15, blank=True, null=True, verbose_name="Teléfono del cliente")
    
    cuarto = models.ForeignKey(Cuarto, on_delete=models.PROTECT, verbose_name="Cuarto reservado")
    fecha_ingreso = models.DateField(verbose_name="Fecha de ingreso")
    fecha_salida = models.DateField(verbose_name="Fecha de salida")
    fecha_reserva = models.DateTimeField(default=timezone.now, verbose_name="Fecha de reserva")

    estado = models.CharField(max_length=10, choices=ESTADO_RESERVA_CHOICES, default='reservado', verbose_name="Estado de la reserva")

    def save(self, *args, **kwargs):
        # Generar un código único si no existe
        if not self.codigo_reserva:
            self.codigo_reserva = self.generar_codigo_reserva()

        # Actualizar disponibilidad del cuarto según el estado
        if self.estado in ['reservado', 'ocupado']:
            self.cuarto.disponible = False
        else:
            self.cuarto.disponible = True
        self.cuarto.save()
        super().save(*args, **kwargs)

    def generar_codigo_reserva(self):
        # Ejemplo: RES-8CARACTERES
        return 'RES-' + uuid.uuid4().hex[:8].upper()

    class Meta:
        verbose_name = "Reserva de Cuarto"
        verbose_name_plural = "Reservas de Cuartos"
        ordering = ['-fecha_reserva']

    def __str__(self):
        return f"{self.codigo_reserva} - {self.nombre_cliente} ({self.estado})"