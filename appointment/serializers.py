from rest_framework import serializers
from .models import  CalismaGunu, Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'baslangic_saati', 'bitis_saati','counselor', 'calisma_gunu']

class CalismaGunuSerializer(serializers.ModelSerializer):
    appointments = AppointmentSerializer(many=True, read_only=True)

    class Meta:
        model = CalismaGunu
        fields = ['id', 'gun', 'baslangic_saati', 'bitis_saati', 'seans_suresi', 'ara_suresi', 'appointments']
