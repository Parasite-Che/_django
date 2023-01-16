from django.db import models
from django.contrib.auth.models import User


class Data(models.Model):
    header = models.CharField(max_length=100)
    document_type = models.CharField(max_length=20)
    theme = models.CharField(max_length=50)
    made_by = models.CharField(max_length=50)
    signed_by = models.CharField(max_length=50)
    date_of_manufacture = models.DateField()
    message = models.CharField(max_length=300)

# Create your models here.
