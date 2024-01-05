# serializers.py
from rest_framework import serializers
from .models import UserProfile

class DanisanSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['age', 'location', 'education']

class UzmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['age', 'location', 'education', 'belge_yukle', 'uzmanlik_alani', 'profil_onay_durumu']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.context['request'].user.is_superuser:
            self.fields.pop('profil_onay_durumu')
