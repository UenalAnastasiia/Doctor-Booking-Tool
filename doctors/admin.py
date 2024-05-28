from django.contrib import admin
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'title', 'speciality')
    list_display = ('id', 'first_name', 'last_name', 'title')
    search_fields = ('last_name',)

admin.site.register(Doctor, DoctorAdmin)