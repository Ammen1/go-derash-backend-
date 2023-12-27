from decimal import Decimal

from django.conf import settings
from django.db import models
from core.checkout.models import DeliveryOptions


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name="order_user")
    delivery_service = models.ForeignKey(
        DeliveryOptions, on_delete=models.CASCADE, related_name="orders")
    email = models.EmailField(max_length=254, blank=True)
    phone = models.CharField(max_length=100)
    total_paid = models.DecimalField(max_digits=5, decimal_places=2)
    order_key = models.CharField(max_length=200)
    payment_option = models.CharField(max_length=200, blank=True)
    billing_status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, choices=[(
        'pending', 'Pending'), ('confirmed', 'Confirmed'), ('completed', 'Completed')])

    class Meta:
        ordering = ("-created",)

    def calculate_total_cost(self):
        # Calculate total cost of all order items
        total_order_cost = sum(item.service_type.calculate_total_cost(
        ) * item.qty for item in self.items.all())

        # Add delivery cost
        total_order_cost += self.delivery_service.calculate_delivery_cost()

        return total_order_cost

    def __str__(self):
        return str(self.status)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name="items", on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Calculate and store the total cost for the order item
        self.total_cost = self.service_type.calculate_total_cost(self.qty)
        self.save()

    def __str__(self):
        return str(self.id)
