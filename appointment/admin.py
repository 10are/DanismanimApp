from django.contrib import admin
from .models import  WorkDay, Appointment

class WorkDayInline(admin.TabularInline):
    model = WorkDay
    extra = 1

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('counselor', 'work_day', 'start_time', 'end_time')
    list_filter = ('counselor', 'work_day')
    search_fields = ('counselor__name', 'counselor__lastname')

admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(WorkDay)
