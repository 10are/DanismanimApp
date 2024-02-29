from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoktorViewSet, CalismaGunuViewSet, RandevuViewSet

router = DefaultRouter()
router.register(r'doktorlar', DoktorViewSet)
router.register(r'calisma_gunleri', CalismaGunuViewSet)
router.register(r'randevular', RandevuViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
