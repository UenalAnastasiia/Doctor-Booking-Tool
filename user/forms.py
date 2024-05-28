from django.contrib.auth.forms import UserCreationForm
from .models import SystemUser


class SystemUserCreationForm(UserCreationForm):
    class Meta:
        model = SystemUser
        fields = '__all__'