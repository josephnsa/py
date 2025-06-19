from django.db import models

class RoomStatus(models.Model):
    status = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.status
