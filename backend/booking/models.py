from django.db import models
from User.models import User
from event.models import Event

"""
Creating a seperate model for booking can be beneficial when you need to track and manage
booking independently from individual tickets; 
also note that ; a ticket can be assigned to only one person and
is independent from the app user; a booking is relatif to the user of the app;

ticket doesn't contain the user id; booking does
"""



class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    booking_quantity = models.PositiveIntegerField()
    PAYMENT_METHOD_CHOICES = [
        ('d17', 'D17'),
        ('master_card', 'Master Card'),
    ]
    booking_payment_method = models.CharField(max_length=100, choices=PAYMENT_METHOD_CHOICES)
