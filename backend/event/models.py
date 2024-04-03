from django.db import models

from user.models import User

class Event(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateField()
    launch_time = models.TimeField()
    available_tickets = models.IntegerField()
    ticket_unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('upcoming', 'Upcoming'), ('finished', 'Finished')])
    people_attending = models.ManyToManyField(User, related_name='events_attending', blank=True)
    registration_link = models.URLField(null=True, blank=True)
    organizer_contact = models.CharField(max_length=100, null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    age_category = models.CharField(max_length=100, null=True, blank=True)
    is_approved = models.BooleanField(default=False)