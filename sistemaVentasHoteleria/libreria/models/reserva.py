from django.db import models
from django.utils import timezone
import uuid
from .cuarto import Cuarto

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
        if not self.codigo_reserva:
            self.codigo_reserva = self.generar_codigo_reserva()

        if self.estado in ['reservado', 'ocupado']:
            self.cuarto.disponible = False
        else:
            self.cuarto.disponible = True
        self.cuarto.save()
        super().save(*args, **kwargs)

    def generar_codigo_reserva(self):
        return 'RES-' + uuid.uuid4().hex[:8].upper()

    class Meta:
        verbose_name = "Reserva de Cuarto"
        verbose_name_plural = "Reservas de Cuartos"
        ordering = ['-fecha_reserva']

    def __str__(self):
        return f"{self.codigo_reserva} - {self.nombre_cliente} ({self.estado})"
