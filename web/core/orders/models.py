from decimal import Decimal

from django.conf import settings
from django.db import models
from core.base.models import ServiceType


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name="order_user")
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

    def __str__(self):
        return str(self.status)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name="items", on_delete=models.CASCADE)
    service_type = models.ForeignKey(
        ServiceType, related_name="order_items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)


class OrderAlert(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
