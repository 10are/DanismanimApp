from django.contrib import admin
from .models import Doktor, CalismaGunu, Randevu

class CalismaGunuInline(admin.TabularInline):
    model = CalismaGunu
    extra = 1

class DoktorAdmin(admin.ModelAdmin):
    list_display = ('adi', 'kullanici')
    inlines = [CalismaGunuInline]

class RandevuAdmin(admin.ModelAdmin):
    list_display = ('doktor', 'calisma_gunu', 'baslangic_saati', 'bitis_saati')
    list_filter = ('doktor', 'calisma_gunu')
    search_fields = ('doktor__adi',)

admin.site.register(Doktor, DoktorAdmin)
admin.site.register(Randevu, RandevuAdmin)
admin.site.register(CalismaGunu)
