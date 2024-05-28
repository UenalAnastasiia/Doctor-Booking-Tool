from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'date', 'created_at', 'doctor', 'id_doctor', 'patient', 'id_patient')
    list_display = ('id', 'date', 'doctor', 'title')
    search_fields = ('doctor', 'patient', 'date',)

admin.site.register(Appointment, AppointmentAdmin)
