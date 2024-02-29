from rest_framework import viewsets
from .models import Doktor, CalismaGunu, Randevu
from .serializers import DoktorSerializer, CalismaGunuSerializer, RandevuSerializer

class DoktorViewSet(viewsets.ModelViewSet):
    queryset = Doktor.objects.all()
    serializer_class = DoktorSerializer

class CalismaGunuViewSet(viewsets.ModelViewSet):
    queryset = CalismaGunu.objects.all()
    serializer_class = CalismaGunuSerializer

class RandevuViewSet(viewsets.ModelViewSet):
    queryset = Randevu.objects.all()
    serializer_class = RandevuSerializer
