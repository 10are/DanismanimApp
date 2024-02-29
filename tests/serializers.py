from rest_framework import serializers
from .models import Doktor, CalismaGunu, Randevu

class RandevuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Randevu
        fields = ['id', 'baslangic_saati', 'bitis_saati']

class CalismaGunuSerializer(serializers.ModelSerializer):
    randevular = RandevuSerializer(many=True, read_only=True)

    class Meta:
        model = CalismaGunu
        fields = ['id', 'gun', 'baslangic_saati', 'bitis_saati', 'seans_suresi', 'ara_suresi', 'randevular']

class DoktorSerializer(serializers.ModelSerializer):
    calisma_gunleri = CalismaGunuSerializer(many=True, read_only=True)

    class Meta:
        model = Doktor
        fields = ['id', 'adi', 'calisma_gunleri']
