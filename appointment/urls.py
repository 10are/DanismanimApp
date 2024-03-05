from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'work-day', views.WorkDayViewSet)
router.register(r'counselor-appointment', views.CounselorAppointmentViewSet)

urlpatterns = [ 
    path('', include(router.urls), name='appointment'),
]
