from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import ConsultantProfile


class ConsultantProfileResource(resources.ModelResource):
    class Meta:
        model = ConsultantProfile

@admin.register(ConsultantProfile)
class ConsultantProfileAdmin(ImportExportModelAdmin):
    list_display = ['user', 'age', 'location', 'education', 'uzmanlik_alani', 'profil_onay_durumu']
    list_filter = ['profil_onay_durumu']

