# views.py
from rest_framework import generics
from .models import UserProfile
from .serializers import DanisanSerializer, UzmanSerializer

class DanisanView(generics.RetrieveUpdateAPIView):
    serializer_class = DanisanSerializer

    def get_object(self):
            user_profile, created = UserProfile.objects.get_or_create(user=self.request.user)
            return user_profile
    
class UzmanView(generics.RetrieveUpdateAPIView):
    serializer_class = UzmanSerializer

    def get_object(self):
        user_profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        return user_profile

    def perform_update(self, serializer):
        if self.request.user.is_superuser:
            serializer.save() 
        else:
            serializer.save(partial=True)  
