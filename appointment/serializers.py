from rest_framework import serializers
from .models import WorkDay, Appointment, Price
from counselor.models import ConsultantProfile


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['id', 'service_name', 'price', 'discount_rate']


class AppointmentSerializer(serializers.ModelSerializer):
    counselor_name = serializers.SerializerMethodField()

    def get_counselor_name(self, obj):
            return obj.counselor.name

    class Meta:
        model = Appointment
        fields = ['id', 'start_time', 'end_time', 'counselor_name',  'work_day']

class WorkDaySerializer(serializers.ModelSerializer):
    appointments = AppointmentSerializer(many=True, read_only=True)
    prices = PriceSerializer(many=True, read_only=True)

    class Meta:
        model = WorkDay
        fields = ['id', 'start_time', 'end_time', 'session_duration', 'break_duration', 'appointments', 'prices']

class CounselorAppointmentSerializer(serializers.ModelSerializer):
    appointments = serializers.SerializerMethodField()
    prices = PriceSerializer(many=True, read_only=True)

    class Meta:
        model = ConsultantProfile
        fields = ['name', 'appointments', 'prices']

    def get_appointments(self, obj):
        appointments = Appointment.objects.filter(counselor=obj)
        return AppointmentSerializer(appointments, many=True).data


