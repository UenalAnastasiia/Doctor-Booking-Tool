from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    birthday = models.DateField()
    
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
