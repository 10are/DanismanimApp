from rest_framework import serializers
from .models import WorkDay, Appointment
from counselor.models import ConsultantProfile

class AppointmentSerializer(serializers.ModelSerializer):
    counselor_name = serializers.SerializerMethodField()

    def get_counselor_name(self, obj):
            return obj.counselor.name

    class Meta:
        model = Appointment
        fields = ['id', 'start_time', 'end_time', 'counselor_name',  'work_day']

class WorkDaySerializer(serializers.ModelSerializer):
    appointments = AppointmentSerializer(many=True, read_only=True)

    class Meta:
        model = WorkDay
        fields = ['id', 'start_time', 'end_time', 'session_duration', 'break_duration', 'appointments']

class CounselorAppointmentSerializer(serializers.ModelSerializer):
    appointments = serializers.SerializerMethodField()

    class Meta:
        model = ConsultantProfile
        fields = ['name', 'appointments']

    def get_appointments(self, obj):
        appointments = Appointment.objects.filter(counselor=obj)
        return AppointmentSerializer(appointments, many=True).data

