# libreria/models/room_maintenance.py

from django.db import models
from .room import Room
from .staff import Staff

class RoomMaintenance(models.Model):
    MAINTENANCE_TYPE_CHOICES = [
        ('preventivo', 'Preventivo'),
        ('correctivo', 'Correctivo'),
    ]

    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='mantenimientos')
    maintenance_type = models.CharField(max_length=20, choices=MAINTENANCE_TYPE_CHOICES)
    description = models.TextField()
    scheduled_start = models.DateField(verbose_name="Inicio Programado")
    scheduled_end = models.DateField(verbose_name="Fin Programado", null=True, blank=True)
    completed = models.BooleanField(default=False)
    responsible_staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Mantenimiento de Cuarto"
        verbose_name_plural = "Mantenimientos de Cuartos"

    def __str__(self):
        return f"{self.room} - {self.maintenance_type} ({'Completado' if self.completed else 'Pendiente'})"
