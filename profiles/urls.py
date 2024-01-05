# urls.py
from django.urls import path
from .views import DanisanView, UzmanView

urlpatterns = [
    path('danisan/', DanisanView.as_view(), name='danisan-profile'),
    path('uzman/', UzmanView.as_view(), name='uzman-profile'),
]
