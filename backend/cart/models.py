from django.db import models
from user.models import User
from event.models import Event


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Event, related_name='carts')  # Assuming events can be added to the cart
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_total_price(self):
        total_price = sum(item.price for item in self.items.all())
        self.total_price = total_price
        self.save()
