from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'phone', 'birthday')
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ('last_name',)

admin.site.register(Patient, PatientAdmin)