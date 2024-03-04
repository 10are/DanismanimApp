from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from counselor.models import ConsultantProfile

class CalismaGunu(models.Model):
    counselor = models.ForeignKey(ConsultantProfile, related_name='calisma_gunu_araliklari', on_delete=models.CASCADE)
    baslangic_tarihi = models.DateField()
    bitis_tarihi = models.DateField()
    baslangic_saati = models.TimeField()
    bitis_saati = models.TimeField()
    seans_suresi = models.IntegerField(help_text="Dakika cinsinden seans süresi")
    ara_suresi = models.IntegerField(help_text="Dakika cinsinden ara süresi")

    def __str__(self):
        return f"{self.counselor.name} - {self.baslangic_tarihi} - {self.bitis_tarihi}"

    def seans_olustur(self):
        gun_sayisi = (self.bitis_tarihi - self.baslangic_tarihi).days + 1
        for gun in range(gun_sayisi):
            calisma_gunu = self.baslangic_tarihi + datetime.timedelta(days=gun)
            baslangic = datetime.datetime.combine(calisma_gunu, self.baslangic_saati)
            bitis = datetime.datetime.combine(calisma_gunu, self.bitis_saati)
            seans_suresi = datetime.timedelta(minutes=self.seans_suresi)
            ara_suresi = datetime.timedelta(minutes=self.ara_suresi)

            while baslangic + seans_suresi <= bitis:
                Appointment.objects.create(
                    counselor=self.counselor,
                    calisma_gunu=calisma_gunu,
                    baslangic_saati=baslangic.time(),
                    bitis_saati=(baslangic + seans_suresi).time()
                )
                baslangic += seans_suresi + ara_suresi



class Appointment(models.Model):
    counselor = models.ForeignKey(ConsultantProfile, related_name='appointments', on_delete=models.CASCADE)
    calisma_gunu = models.DateField()
    baslangic_saati = models.TimeField()
    bitis_saati = models.TimeField()

    def __str__(self):
        return f"{self.counselor.name} - {self.calisma_gunu} - {self.baslangic_saati} - {self.bitis_saati}"

@receiver(post_save, sender=CalismaGunu)
def seanslari_olustur(sender, instance, created, **kwargs):
    if created:
        instance.seans_olustur()
