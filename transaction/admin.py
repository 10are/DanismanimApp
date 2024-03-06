from django.contrib import admin
from .models import *

class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    extra = 1
    list_display = ['client', 'appointment']


admin.site.register(Transaction, TransactionAdmin)
