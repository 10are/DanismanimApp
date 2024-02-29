from django.contrib import admin
from .models import Doktor, CalismaGunu, Randevu

class RandevuInline(admin.TabularInline):
    model = Randevu
    extra = 0 

class CalismaGunuAdmin(admin.ModelAdmin):
    list_display = ('doktor', 'gun', 'baslangic_saati', 'bitis_saati', 'seans_suresi', 'ara_suresi')
    list_filter = ('doktor', 'gun')

class RandevuAdmin(admin.ModelAdmin):
    list_display = ('calisma_gunu', 'baslangic_saati', 'bitis_saati', 'doktor_adi')
    list_filter = ('calisma_gunu__doktor', 'calisma_gunu__gun')
    search_fields = ('calisma_gunu__doktor__adi',)

    def doktor_adi(self, obj):
        return obj.calisma_gunu.doktor.adi
    doktor_adi.admin_order_field = 'calisma_gunu__doktor'  
    doktor_adi.short_description = 'Doktor Adı' 

class DoktorAdmin(admin.ModelAdmin):
    list_display = ('adi', 'kullanici')
    search_fields = ('adi',)

admin.site.register(Doktor, DoktorAdmin)
admin.site.register(CalismaGunu, CalismaGunuAdmin)
admin.site.register(Randevu, RandevuAdmin) 
