from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import SystemUserCreationForm
from .models import SystemUser

@admin.register(SystemUser)
class CustomUserAdmin(admin.ModelAdmin):
    add_form = SystemUserCreationForm
    fieldsets = (
        *UserAdmin.fieldsets, 
        (
            'Position',
            {
                'fields': (
                    'doctor',
                    'patient',
                )
            }
        )
    )