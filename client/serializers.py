from rest_framework import serializers
from .models import ClientProfile

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = ['age', 'location', 'education', 'profile_picture']