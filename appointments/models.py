from django.db import models
import datetime
from doctors.models import Doctor
from patients.models import Patient


class Appointment(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date = models.DateField()
    created_at = models.DateField(default=datetime.date.today)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    id_doctor = models.CharField(max_length=100)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    id_patient = models.CharField(max_length=100)
    
    
    def doctor_name(self):
        return f"{self.doctor.get_title_display()} {self.doctor.first_name} {self.doctor.last_name}"

        
    def patient_name(self):
        return self.patient.first_name + ' ' + self.patient.last_name