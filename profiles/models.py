# models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    EDU_CHOICES = (
        ('High School', 'High School'),
        ('College', 'College'),
        ('Graduate School', 'Graduate School'),

    )


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.CharField(max_length=10, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    education = models.CharField(max_length=50, choices=EDU_CHOICES, blank=True, null=True)
    belge_yukle = models.FileField(upload_to='files/', max_length=50,  blank=True, null=True)
    uzmanlik_alani = models.CharField(max_length=50, blank=True, null=True)
    profil_onay_durumu = models.BooleanField(default=False)
