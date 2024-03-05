from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import WorkDay

@receiver(post_save, sender=WorkDay)
def create_sessions(sender, instance, created, **kwargs):
    if created:
        instance.create_sessions()
