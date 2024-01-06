# views.py
from rest_framework import generics
from .models import ConsultantProfile
from .serializers import ConsultantSerializer

class ConsultanView(generics.RetrieveUpdateAPIView):
    serializer_class = ConsultantSerializer

    def get_object(self):
        user_profile, created = ConsultantProfile.objects.get_or_create(user=self.request.user)
        return user_profile

    def perform_update(self, serializer):
        if self.request.user.is_superuser:
            serializer.save() 
        else:
            serializer.save(partial=True)  
