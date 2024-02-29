from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

class Doktor(models.Model):
    kullanici = models.OneToOneField(User, on_delete=models.CASCADE)
    adi = models.CharField(max_length=100)

    def __str__(self):
        return self.adi

class CalismaGunu(models.Model):
    doktor = models.ForeignKey(Doktor, related_name='calisma_gunleri', on_delete=models.CASCADE)
    gun = models.DateField()
    baslangic_saati = models.TimeField()
    bitis_saati = models.TimeField()
    seans_suresi = models.IntegerField(help_text="Dakika cinsinden seans süresi")
    ara_suresi = models.IntegerField(help_text="Dakika cinsinden ara süresi")

    def __str__(self):
        return f"{self.doktor.adi} - {self.gun}"

    def seans_olustur(self):
        baslangic = datetime.datetime.combine(self.gun, self.baslangic_saati)
        bitis = datetime.datetime.combine(self.gun, self.bitis_saati)
        seans_suresi = datetime.timedelta(minutes=self.seans_suresi)
        ara_suresi = datetime.timedelta(minutes=self.ara_suresi)

        while baslangic + seans_suresi <= bitis:
            Randevu.objects.create(
                calisma_gunu=self,
                baslangic_saati=baslangic.time(),
                bitis_saati=(baslangic + seans_suresi).time()
            )
            baslangic += seans_suresi + ara_suresi

class Randevu(models.Model):
    calisma_gunu = models.ForeignKey(CalismaGunu, related_name='randevular', on_delete=models.CASCADE)
    baslangic_saati = models.TimeField()
    bitis_saati = models.TimeField()

    def __str__(self):
        return f"{self.calisma_gunu.doktor.adi} - {self.baslangic_saati} - {self.bitis_saati}"

@receiver(post_save, sender=CalismaGunu)
def seanslari_olustur(sender, instance, created, **kwargs):
    if created:
        instance.seans_olustur()
