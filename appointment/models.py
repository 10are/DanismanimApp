from django.contrib.auth.models import User
from counselor.models import ConsultantProfile
import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Price(models.Model):
    counselor = models.ForeignKey(ConsultantProfile, related_name='prices', on_delete=models.CASCADE)
    service_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, help_text="Discount rate in percentage")

    def __str__(self):
        return f"{self.service_name} - {self.price} - {self.discount_rate}%"

class WorkDay(models.Model):
    counselor = models.ForeignKey(ConsultantProfile, related_name='work_day', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    session_duration = models.IntegerField(help_text="Session duration in minutes")
    break_duration = models.IntegerField(help_text="Break duration in minutes")
    price = models.OneToOneField(Price, related_name='work_day', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('counselor', 'start_date', 'end_date', 'start_time', 'end_time')

    def __str__(self):
        return f"{self.counselor.name} - {self.start_date} - {self.end_date}"

    def create_sessions(self):
        if self.start_date > self.end_date or (self.start_date == self.end_date and self.start_time >= self.end_time):
            raise ValidationError(_("Start date and time cannot be after or equal to end date and time."))

        days_count = (self.end_date - self.start_date).days + 1
        for day in range(days_count):
            work_day = self.start_date + datetime.timedelta(days=day)
            if work_day > self.end_date:
                break
            start_time = datetime.datetime.combine(work_day, self.start_time)
            end_time = datetime.datetime.combine(work_day, self.end_time)
            session_duration = datetime.timedelta(minutes=self.session_duration)
            break_duration = datetime.timedelta(minutes=self.break_duration)

            while start_time + session_duration <= end_time:
                existing_appointments = Appointment.objects.filter(
                    counselor=self.counselor,
                    work_day=work_day,
                    start_time=start_time.time(),
                    end_time=(start_time + session_duration).time()
                )
                if existing_appointments.exists():
                    raise ValidationError(_("Bu saat diliminde zaten bir randevunuz bulunmaktadır. Lütfen başka bir saat dilimi seçin."))

                Appointment.objects.create(
                    counselor=self.counselor,
                    work_day=work_day,
                    start_time=start_time.time(),
                    end_time=(start_time + session_duration).time()
                )
                start_time += session_duration + break_duration

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Sold', 'Sold'),  
    ]

    counselor = models.ForeignKey(ConsultantProfile, related_name='appointments', on_delete=models.CASCADE)
    work_day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')  
    Price = models.ForeignKey(Price, related_name='appointments', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.counselor.name} - {self.work_day} - {self.start_time} - {self.end_time}"
