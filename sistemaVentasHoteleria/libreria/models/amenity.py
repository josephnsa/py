from django.db import models


class Amenity(models.Model):
    name = models.CharField(max_length=50, unique=True)
    icon = models.CharField(max_length=50, blank=True)  # Ej. 'fa fa-wifi'

    def __str__(self):
        return self.name


class RoomAmenity(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('room', 'amenity')
