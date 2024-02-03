from rest_framework import generics
from .models import Randevu
from .serializers import RandevuSerializer

class RandevuListCreateView(generics.ListCreateAPIView):
    queryset = Randevu.objects.all()
    serializer_class = RandevuSerializer

class RandevuRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Randevu.objects.all()
    serializer_class = RandevuSerializer
