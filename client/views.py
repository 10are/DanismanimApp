from rest_framework import generics
from .models import ClientProfile
from .serializers import ClientSerializer

class ClientView(generics.RetrieveUpdateAPIView):
    serializer_class = ClientSerializer

    def get_object(self):
            user_profile, created = ClientProfile.objects.get_or_create(user=self.request.user)
            return user_profile
    