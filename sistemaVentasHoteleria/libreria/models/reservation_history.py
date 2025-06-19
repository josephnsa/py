# libreria/models/reservation_history.py

from django.db import models
from .reservation import RoomReservation
from .staff import Staff

class ReservationHistory(models.Model):
    STATUS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmado', 'Confirmado'),
        ('checkin', 'Check-in'),
        ('checkout', 'Check-out'),
        ('cancelado', 'Cancelado'),
    ]

    reservation = models.ForeignKey(RoomReservation, on_delete=models.CASCADE, related_name='historial')
    previous_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    new_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    changed_by = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Historial de Reserva"
        verbose_name_plural = "Historial de Reservas"
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.reservation} - {self.previous_status} → {self.new_status}"
