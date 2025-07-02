from django.db import models
from django.utils import timezone

class RoomInspectionReport(models.Model):
    reservation = models.OneToOneField(
        'RoomReservation',
        on_delete=models.CASCADE,
        verbose_name="Reserva Asociada"
    )
    room = models.ForeignKey(
        'Room',
        on_delete=models.CASCADE,
        verbose_name="Cuarto Inspeccionado"
    )
    category = models.ForeignKey(
        'RoomCategory',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Categoría del Cuarto"
    )

    estado_general = models.CharField(
        max_length=100,
        choices=[
            ('bueno', 'Bueno'),
            ('regular', 'Regular'),
            ('malo', 'Malo'),
        ],
        default='bueno',
        verbose_name="Estado General del Cuarto"
    )

    observaciones_piso = models.TextField(blank=True, null=True, verbose_name="Observaciones del Piso")
    observaciones_paredes = models.TextField(blank=True, null=True, verbose_name="Observaciones de las Paredes")
    observaciones_muebles = models.TextField(blank=True, null=True, verbose_name="Observaciones de Mobiliario")
    observaciones_servicios = models.TextField(blank=True, null=True, verbose_name="Servicios (TV, agua, luz, etc.)")
    limpieza_general = models.TextField(blank=True, null=True, verbose_name="Observaciones de Limpieza")
    otros_detalles = models.TextField(blank=True, null=True, verbose_name="Otros Detalles")

    evidencia_1 = models.ImageField(upload_to='room_inspections/', blank=True, null=True, verbose_name="Evidencia 1")
    evidencia_2 = models.ImageField(upload_to='room_inspections/', blank=True, null=True, verbose_name="Evidencia 2")
    evidencia_3 = models.ImageField(upload_to='room_inspections/', blank=True, null=True, verbose_name="Evidencia 3")

    creado_en = models.DateTimeField(default=timezone.now, verbose_name="Fecha del Reporte")

    class Meta:
        verbose_name = "Informe de Inspección del Cuarto"
        verbose_name_plural = "Informes de Inspección de Cuartos"
        ordering = ['-creado_en']

    def __str__(self):
        return f"Inspección de {self.room} ({self.reservation.code})"
