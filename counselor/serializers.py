from rest_framework import serializers
from .models import ConsultantProfile

class ConsultantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultantProfile
        fields = ['name', 'lastname', 'age', 'location', 'education', 'belge_yukle', 'uzmanlik_alani', 'profil_onay_durumu', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.context['request'].user.is_superuser:
            self.fields.pop('profil_onay_durumu')
