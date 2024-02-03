from django.urls import path
from .views import RandevuListCreateView, RandevuRetrieveUpdateDestroyView

urlpatterns = [
    path('randevular/', RandevuListCreateView.as_view(), name='randevu-list-create'),
    path('randevular/<int:pk>/', RandevuRetrieveUpdateDestroyView.as_view(), name='randevu-retrieve-update-destroy'),
]
