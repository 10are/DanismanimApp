from django.urls import path
from .views import ConsultanView

urlpatterns = [
    path('', ConsultanView.as_view(), name='danisan-profile'),
]
