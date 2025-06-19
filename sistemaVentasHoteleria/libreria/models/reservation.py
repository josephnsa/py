from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid
from .room import Room
from .customer import Customer

RESERVATION_STATUS = [
    ('reservado', 'Reservado'),
    ('ocupado', 'Ocupado'),
    ('cancelado', 'Cancelado'),
    ('finalizado', 'Finalizado'),
]

class RoomReservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.CharField(max_length=12, unique=True, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=15, choices=RESERVATION_STATUS, default='reservado')
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = 'RES-' + uuid.uuid4().hex[:8].upper()
        # Actualiza disponibilidad del cuarto
        self.room.available = False if self.status in ['reservado', 'ocupado'] else True
        self.room.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.code} - {self.customer.full_name}"
