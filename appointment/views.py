from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import CalismaGunu, Appointment
from .serializers import CalismaGunuSerializer, AppointmentSerializer



class CalismaGunuViewSet(viewsets.ModelViewSet):
    queryset = CalismaGunu.objects.all()
    serializer_class = CalismaGunuSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
