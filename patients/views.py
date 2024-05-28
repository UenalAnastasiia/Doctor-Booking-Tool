from rest_framework import status
from rest_framework.views import APIView
from .serializers import PatientSerializer
from .models import Patient
from rest_framework.response import Response


class PatientViewSet(APIView):    
    def get(self, request, format=None):
        patient_list = Patient.objects.all()
        serializer = PatientSerializer(patient_list, many=True)
        return Response(serializer.data)
    
    
    def post(self, request, format=None):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class PatientDetailsViewSet(APIView):
    def get(self, request, pk):
        try:
            patient_object = Patient.objects.filter(id=pk)
            serializer = PatientSerializer(patient_object, many=True)
            return Response(serializer.data)
        except Patient.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    
    
    def get_queryset(self, pk):
        try:
            patient_object = Patient.objects.get(id=pk)
            return patient_object
        except Patient.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    
    def delete(self, request, pk, format=None):
        patient_object = self.get_queryset(pk)
        patient_object.delete()
        return Response(status.HTTP_204_NO_CONTENT)