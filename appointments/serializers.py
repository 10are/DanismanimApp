from rest_framework import serializers
from .models import Randevu

class RandevuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Randevu
        fields = '__all__'
