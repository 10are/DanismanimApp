from rest_framework import serializers
from .models import  CalismaGunu, Appointment
from counselor.models import ConsultantProfile

class AppointmentSerializer(serializers.ModelSerializer):
    counselor_name = serializers.SerializerMethodField()

    def get_counselor_name(self, obj):
            return obj.counselor.name

    class Meta:
        model = Appointment
        fields = ['id', 'baslangic_saati', 'bitis_saati', 'counselor_name',  'calisma_gunu']

class CalismaGunuSerializer(serializers.ModelSerializer):
    appointments = AppointmentSerializer(many=True, read_only=True)

    class Meta:
        model = CalismaGunu
        fields = ['id', 'baslangic_saati', 'bitis_saati', 'seans_suresi', 'ara_suresi', 'appointments']

class CounselorAppointmentSerializer(serializers.ModelSerializer):
    appointments = serializers.SerializerMethodField()

    class Meta:
        model = ConsultantProfile
        fields = ['name', 'appointments']

    def get_appointments(self, obj):
        appointments = Appointment.objects.filter(counselor=obj)
        return AppointmentSerializer(appointments, many=True).data
