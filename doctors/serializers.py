from rest_framework import serializers
from .models import Choices, Doctor


class ChoiceField(serializers.ChoiceField):
    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)
        
        
class DoctorSerializer(serializers.ModelSerializer ):
    title = ChoiceField(choices=Choices.TITLE_LIST)
    speciality = ChoiceField(choices=Choices.SPECIALITY_LIST)
    
    class Meta:
        model = Doctor
        fields = '__all__'