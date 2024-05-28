from rest_framework import serializers
from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ['id', 'title', 'description', 'date', 'doctor_name', 'patient_name', 'created_at']
        
    