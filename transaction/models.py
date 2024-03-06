from django.db import models
from appointment.models import Appointment
from client.models import ClientProfile

class Transaction(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)

    
    class Meta:
            unique_together = ('client', 'appointment')

    def __str__(self):
        return self.client.user.username
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.appointment.status = 'Sold'
        self.appointment.save()

    
    
