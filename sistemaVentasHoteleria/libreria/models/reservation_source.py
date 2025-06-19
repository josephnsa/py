from django.db import models


class ReservationSource(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Ej: Web, Recepción, Booking

    def __str__(self):
        return self.name
