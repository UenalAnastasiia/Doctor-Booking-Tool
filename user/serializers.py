from rest_framework import serializers
from .models import SystemUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemUser
        fields = '__all__'
        
    # def __str__(self):
    #     return self.username