from django.db import models
from .reservation import RoomReservation

class Payment(models.Model):
    reservation = models.ForeignKey(RoomReservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=20, choices=[
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('yape', 'Yape'),
        ('plin', 'Plin'),
    ])

    def __str__(self):
        return f"{self.reservation.code} - {self.amount}"
