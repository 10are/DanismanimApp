from rest_framework import serializers
from .models import ClientProfile

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = ['name', 'lastname', 'age', 'location', 'education', 'profile_picture']