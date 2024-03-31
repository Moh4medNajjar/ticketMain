from django.db import models
from event.models import Event

class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='ticket_qrcodes/')
    buy_time = models.TimeField()
    buy_date = models.DateField()
    seat_number = models.CharField(max_length=20, blank=True, null=True)  # Optional seat number field


"""
    We do not need to put the holder name on the ticket, tickets for most
    events are transferable.

"""
