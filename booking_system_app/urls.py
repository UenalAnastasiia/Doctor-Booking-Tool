"""
URL configuration for booking_system_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appointments.views import AppointmentDetailsViewSet, AppointmentViewSet
from doctors.views import DoctorDetailsViewSet, DoctorViewSet
from patients.views import PatientDetailsViewSet, PatientViewSet
from user.views import UserViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/doctors/', DoctorViewSet.as_view()),
    path('api/doctors/<int:pk>/', DoctorDetailsViewSet.as_view()),
    path('api/patients/', PatientViewSet.as_view()),
    path('api/patients/<int:pk>/', PatientDetailsViewSet.as_view()),
    path('api/appointments/', AppointmentViewSet.as_view()),
    path('api/appointments/<int:pk>/', AppointmentDetailsViewSet.as_view()),
    path('api/users/', UserViewSet.as_view()),
]