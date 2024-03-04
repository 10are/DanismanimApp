from django.contrib import admin
from .models import  CalismaGunu, Appointment

class CalismaGunuInline(admin.TabularInline):
    model = CalismaGunu
    extra = 1


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('counselor', 'calisma_gunu', 'baslangic_saati', 'bitis_saati')
    list_filter = ('counselor', 'calisma_gunu')
    search_fields = ('counselor__name', 'counselor__lastname')

admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(CalismaGunu)
