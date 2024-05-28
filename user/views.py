from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SystemUser
from .serializers import UserSerializer

class UserViewSet(APIView):    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        if request.user.is_superuser:
            appointment_list = SystemUser.objects.all()
            serializer = UserSerializer(appointment_list, many=True)
            return Response(serializer.data)
