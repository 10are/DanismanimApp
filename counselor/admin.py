from django.contrib import admin
from .models import ConsultantProfile  

@admin.register(ConsultantProfile)
class ConsultantProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'location', 'education', 'uzmanlik_alani', 'profil_onay_durumu']
    list_filter = ['profil_onay_durumu']

