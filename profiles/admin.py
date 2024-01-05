# admin.py
from django.contrib import admin
from .models import UserProfile  

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'location', 'education', 'uzmanlik_alani', 'profil_onay_durumu']
    list_filter = ['profil_onay_durumu']