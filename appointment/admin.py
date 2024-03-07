from django.contrib import admin
from .models import WorkDay, Appointment, Price

class WorkDayInline(admin.TabularInline):
    model = WorkDay
    extra = 1

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('counselor', 'work_day', 'start_time', 'end_time', 'get_price')
    list_filter = ('counselor', 'work_day')

    def get_price(self, obj):
        return obj.counselor.prices.first().price if obj.counselor.prices.exists() else None

    get_price.short_description = 'Price'

class PriceAdmin(admin.ModelAdmin):
    list_display = ('counselor', 'service_name', 'price', 'discount_rate')
    list_filter = ('counselor',)
    search_fields = ('counselor__name', 'service_name')

admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(WorkDay)
admin.site.register(Price, PriceAdmin)
