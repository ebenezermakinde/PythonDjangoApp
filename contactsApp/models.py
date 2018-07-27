from django.db import models
from datetime import datetime

# Create your models here.

class contactsApp(models.Model):
    name = models.CharField(max_length=220)
    email = models.CharField(max_length=60, unique=True)
    dateCreated = models.DateTimeField(default=datetime.now, blank=True)
    dateUpdated = models.DateTimeField(default=datetime.now, blank=True)

