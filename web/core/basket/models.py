from decimal import Decimal
from django.conf import settings
from django.db import models
from core.checkout.models import DeliveryOptions
from core.base.models import ServiceType


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    services = models.ManyToManyField(ServiceType)
    delivery_option = models.ForeignKey(
        DeliveryOptions, on_delete=models.SET_NULL, null=True)

    def get_subtotal_price(self):
        return sum(service_type.service.regular_price for service_type in self.services.all())

    def get_delivery_price(self):
        return self.delivery_option.delivery_price if self.delivery_option else 0.0

    def get_total_price(self):
        subtotal = self.get_subtotal_price()
        delivery_price = self.get_delivery_price()
        return subtotal + Decimal(delivery_price)
