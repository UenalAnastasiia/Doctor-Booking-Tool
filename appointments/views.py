from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import AppointmentSerializer
from .models import Appointment
from rest_framework.response import Response


class AppointmentViewSet(APIView):    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        if request.user.is_superuser:
            appointment_list = Appointment.objects.all()
            serializer = AppointmentSerializer(appointment_list, many=True)
            return Response(serializer.data)
        elif request.user.doctor:
            appointment_list = Appointment.objects.filter(id_doctor=request.user.id)
            serializer = AppointmentSerializer(appointment_list, many=True)
            return Response(serializer.data)
        elif request.user.patient:
            appointment_list = Appointment.objects.filter(id_patient=request.user.id)
            serializer = AppointmentSerializer(appointment_list, many=True)
            return Response(serializer.data)
            
    
    
    def post(self, request, format=None):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class AppointmentDetailsViewSet(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):   
        try:
            if request.user.is_superuser:
                appointment_object = Appointment.objects.get(id=pk)
                serializer = AppointmentSerializer(appointment_object)
                return Response(serializer.data)
            elif request.user.doctor:
                appointment_object = Appointment.objects.get(id=pk, id_doctor=request.user.id)
                serializer = AppointmentSerializer(appointment_object)
                return Response(serializer.data)
            elif request.user.patient:
                appointment_object = Appointment.objects.get(id=pk, id_patient=request.user.id)
                serializer = AppointmentSerializer(appointment_object)
                return Response(serializer.data)
        except Appointment.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
    
    
    def get_queryset(self, pk):
        try:
            appointment_object = Appointment.objects.get(id=pk)
            return appointment_object
        except Appointment.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        
    
    def delete(self, request, pk, format=None):
        appointment_object = self.get_queryset(pk)
        if request.user.is_superuser:
            print('DELETE', appointment_object)
            appointment_object.delete()
            return Response(status.HTTP_204_NO_CONTENT)
        else:
            return Response(status.HTTP_404_NOT_FOUND)