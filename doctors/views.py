from rest_framework import status
from rest_framework.views import APIView
from .serializers import DoctorSerializer
from .models import Doctor
from rest_framework.response import Response


class DoctorViewSet(APIView):    
    def get(self, request, format=None):
        doctor_list = Doctor.objects.all()
        serializer = DoctorSerializer(doctor_list, many=True)
        return Response(serializer.data)
    
    
    def post(self, request, format=None):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class DoctorDetailsViewSet(APIView):
    def get(self, request, pk):
        try:
            doctor_object = Doctor.objects.filter(id=pk)
            serializer = DoctorSerializer(doctor_object, many=True)
            return Response(serializer.data)
        except Doctor.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    
    
    def get_queryset(self, pk):
        try:
            doctor_object = Doctor.objects.get(id=pk)
            return doctor_object
        except Doctor.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    
    def delete(self, request, pk, format=None):
        doctor_object = self.get_queryset(pk)
        doctor_object.delete()
        return Response(status.HTTP_204_NO_CONTENT)