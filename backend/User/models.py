from django.db import models

class User(models.Model):
    age = models.PositiveIntegerField(null=True)
    field_of_interest = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(unique=True)
    governorate = models.CharField(max_length=100, null=True)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
