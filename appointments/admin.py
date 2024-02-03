from django.contrib import admin
from .models import Randevu



class RandevuAdmin(admin.ModelAdmin):
    field = '__all__'

admin.site.register(Randevu)
