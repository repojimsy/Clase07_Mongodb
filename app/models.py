from django.db import models

class doctor(models.Model):
    nombre = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=30)
