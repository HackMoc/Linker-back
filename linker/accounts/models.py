from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=16, unique=True)
    email = models.EmailField(max_length=255, unique=True)

