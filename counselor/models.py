from django.db import models
from django.contrib.auth.models import User

class ConsultantProfile(models.Model):
    EDU_CHOICES = (
        ('1', 'İlkokul'),
        ('2', 'Ortaokul'),
        ('3', 'Lise'),
        ('4', 'Üniversite'),
        ('5', 'Yüksek Lisans'),
        ('6', 'Doktora'),
    )

    LOCATION_CHOICES = (
        ('IST', 'İstanbul'),
        ('ANK', 'Ankara'),
        ('IZM', 'İzmir'),
        ('ADN', 'Adana'),
        ('ANT', 'Antalya'),
        ('BAL', 'Balıkesir'),
        ('BRS', 'Bursa'),
        ('ESK', 'Eskişehir'),
        ('KOC', 'Kocaeli'),
        ('KON', 'Konya'),
        ('MRS', 'Mersin'),
        ('SIV', 'Sivas'),
        ('TRB', 'Trabzon'),
        ('ZNG', 'Zonguldak'),
        ('OTH', 'Diğer'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, blank=True, null=True)
    education = models.CharField(max_length=50, choices=EDU_CHOICES, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    belge_yukle = models.FileField(upload_to='files/', max_length=50,  blank=True, null=True)
    uzmanlik_alani = models.CharField(max_length=50, blank=True, null=True)
    profil_onay_durumu = models.BooleanField(default=False)
