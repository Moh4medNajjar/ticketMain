from event.models import Event
from django.db import models
from user.models import User

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    booking_quantity = models.IntegerField()
    booking_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_payment_method = models.CharField(max_length=100)
    booking_payment_status = models.CharField(max_length=20)