from django.db import models

class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    password = models.CharField(max_length=100)
    field_of_interest = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    governate = models.CharField(max_length=100)
    # booked_events = models.ManyToManyField('Event', related_name='booked_users')
    is_verified = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Add MFA fields
    mfa_enabled = models.BooleanField(default=False)
    mfa_secret_key = models.CharField(max_length=100, blank=True, null=True)

