# models.py

from django.db import models
from django.utils import timezone
import uuid
from django.conf import settings
from .room import Room  # Asegúrate de importar bien

RESERVATION_STATUS = [
    ('reservado', 'Reservado'),
    ('ocupado', 'Ocupado'),
    ('cancelado', 'Cancelado'),
    ('finalizado', 'Finalizado'),
]

class RoomReservation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        verbose_name="Registrado por"
    )
    
    code = models.CharField(
        max_length=12, 
        unique=True, 
        editable=False,
        verbose_name="Código de Reserva"
    )

    # Datos del cliente
    customer_name = models.CharField(max_length=100, verbose_name="Nombre del cliente")
    customer_document = models.CharField(max_length=30, null=True, blank=True)
    customer_email = models.EmailField(blank=True, null=True, verbose_name="Correo")
    customer_phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Teléfono")

    # Datos de reserva
    room = models.ForeignKey(Room, on_delete=models.PROTECT, verbose_name="Cuarto reservado")
    check_in = models.DateField(verbose_name="Fecha de ingreso")
    check_out = models.DateField(verbose_name="Fecha de salida")
    status = models.CharField(
        max_length=15, 
        choices=RESERVATION_STATUS, 
        default='reservado',
        verbose_name="Estado"
    )
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Fecha de reserva")

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generar_codigo()
        self.room.available = self.status not in ['reservado', 'ocupado']
        self.room.save()
        super().save(*args, **kwargs)

    def generar_codigo(self):
        return 'RES-' + uuid.uuid4().hex[:8].upper()

    def __str__(self):
        return f"{self.code} - {self.customer_name} ({self.get_status_display()})"

    class Meta:
        verbose_name = "Reserva de Cuarto"
        verbose_name_plural = "Reservas de Cuartos"
        ordering = ['-created_at']
