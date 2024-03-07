from rest_framework import viewsets
from .models import WorkDay, Appointment, Price
from .serializers import WorkDaySerializer, AppointmentSerializer, CounselorAppointmentSerializer, PriceSerializer
from counselor.models import ConsultantProfile

class WorkDayViewSet(viewsets.ModelViewSet):
    queryset = WorkDay.objects.all()
    serializer_class = WorkDaySerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class CounselorAppointmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ConsultantProfile.objects.all()
    serializer_class = CounselorAppointmentSerializer

class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
