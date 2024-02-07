from django.contrib import admin
from .models import Blog
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = '__all__'

class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    list_display = 'title', 'author', 'created_at', 'updated_at'

admin.site.register(Blog, BlogAdmin)
