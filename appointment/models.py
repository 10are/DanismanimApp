from django.contrib.auth.models import User
from counselor.models import ConsultantProfile
import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class WorkDay(models.Model):
    counselor = models.ForeignKey(ConsultantProfile, related_name='work_day_ranges', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    session_duration = models.IntegerField(help_text="Session duration in minutes")
    break_duration = models.IntegerField(help_text="Break duration in minutes")

    def __str__(self):
        return f"{self.counselor.name} - {self.start_date} - {self.end_date}"

    def create_sessions(self):
        if self.start_date > self.end_date:
            raise ValidationError(_("Start date cannot be after end date."))

        if self.start_time >= self.end_time:
            raise ValidationError(_("Start time cannot be after or equal to end time."))

        days_count = (self.end_date - self.start_date).days + 1
        for day in range(days_count):
            work_day = self.start_date + datetime.timedelta(days=day)
            if work_day > self.end_date:
                break  # Son tarihden sonra çalışmayı durdur
            start_time = datetime.datetime.combine(work_day, self.start_time)
            end_time = datetime.datetime.combine(work_day, self.end_time)
            session_duration = datetime.timedelta(minutes=self.session_duration)
            break_duration = datetime.timedelta(minutes=self.break_duration)

            while start_time + session_duration <= end_time:
                Appointment.objects.create(
                    counselor=self.counselor,
                    work_day=work_day,
                    start_time=start_time.time(),
                    end_time=(start_time + session_duration).time()
                )
                start_time += session_duration + break_duration


class Appointment(models.Model):
    counselor = models.ForeignKey(ConsultantProfile, related_name='appointments', on_delete=models.CASCADE)
    work_day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.counselor.name} - {self.work_day} - {self.start_time} - {self.end_time}"
