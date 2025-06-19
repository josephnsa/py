# libreria/models/room_change_log.py

from django.db import models
from .room import Room
from .room_status import RoomStatus
from .staff import Staff

class RoomChangeLog(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='cambios_estado')
    previous_status = models.ForeignKey(RoomStatus, on_delete=models.SET_NULL, null=True, related_name='+')
    new_status = models.ForeignKey(RoomStatus, on_delete=models.SET_NULL, null=True, related_name='+')
    changed_by = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Cambio de Estado del Cuarto"
        verbose_name_plural = "Historial de Estado de Cuartos"
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.room} - {self.previous_status} → {self.new_status} ({self.timestamp})"
