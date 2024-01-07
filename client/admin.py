from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import ClientProfile

class ClientProfileResource(resources.ModelResource):
    class Meta:
        model = ClientProfile

@admin.register(ClientProfile)
class ClientProfileAdmin(ImportExportModelAdmin):
    resource_class = ClientProfileResource
    list_display = ['user', 'age', 'location', 'education']

