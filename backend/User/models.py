from django.db import models
from django.contrib.auth.hashers import make_password
class User(models.Model):
    username = models.CharField(max_length=150, unique=True,default="")
    password = models.CharField(max_length=128, default="")
    age = models.PositiveIntegerField(null=True)
    field_of_interest = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(unique=True)
    governorate = models.CharField(max_length=100, null=True)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    #MFA fields
    mfa_enabled = models.BooleanField(default=False) 
    mfa_secret_key = models.CharField(max_length=100, null=True)

    def save(self, *args, **kwargs):
        # Hash the password before saving
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
