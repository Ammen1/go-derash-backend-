from decimal import Decimal
from core.base.models import Product, ProductSpecification
from django.conf import settings
from django.db import models
from core.checkout.models import DeliveryOptions


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name="orders")
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2)
    order_key = models.CharField(max_length=200)
    payment_option = models.CharField(
        max_length=200, choices=[("option1", "Option 1"), ("option2", "Option 2")], blank=True)
    billing_status = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return str(self.created)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE)
    # spification = models.ForeignKey(ProductSpecification)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
