from django.db import models

# Create your models here.

class Practitioner(models.Model):
    name = models.CharField(max_length=100)
    identifier = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    # Add other fields as per the FHIR specification

    def __str__(self):
        return self.name

