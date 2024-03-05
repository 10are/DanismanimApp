from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import WorkDay, Appointment
from .serializers import WorkDaySerializer, AppointmentSerializer ,CounselorAppointmentSerializer
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

