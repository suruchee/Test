from rest_framework import serializers
from .models import Practitioner

class PractitionerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practitioner
        fields = '__all__'
