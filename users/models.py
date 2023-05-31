from django.db import models

# Create your models here.

class User(models.Model):
     first_name = models.CharField(max_length=255)
     last_name = models.CharField(max_length=255)
     password = models.CharField(max_length=255)
     year = models.IntegerField()
     token = models.CharField(max_length=255)

