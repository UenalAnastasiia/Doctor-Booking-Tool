from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class SystemUser(AbstractUser):
    doctor = models.BooleanField(default=False, null=True)
    patient = models.BooleanField(default=False, null=True)