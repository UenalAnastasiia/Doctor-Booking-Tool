from django.db import models


class Choices(models.Model):
    TITLE_LIST = ((1, 'Dr.'), (2, 'Prof. Dr.'), (3, 'Dr. rer. nat.'))
    SPECIALITY_LIST = ((1, 'Allgemeinmedizin'), (2, 'Radiologe'), (3, 'Hautarzt'))
    

class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.IntegerField(choices=Choices.TITLE_LIST)
    speciality = models.IntegerField(choices=Choices.SPECIALITY_LIST)
    
    
    def __str__(self):
        return f"{self.get_title_display()} {self.first_name} {self.last_name}"