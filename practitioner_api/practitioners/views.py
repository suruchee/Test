from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Practitioner
from .serializers import PractitionerSerializer


class PractitionerViewSet(viewsets.ModelViewSet):
    queryset = Practitioner.objects.all()
    serializer_class = PractitionerSerializer


