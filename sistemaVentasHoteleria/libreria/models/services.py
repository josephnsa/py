from django.db import models
from .room import Room

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class RoomService(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('room', 'service')

    def __str__(self):
        return f"{self.room.number} - {self.service.name}"
