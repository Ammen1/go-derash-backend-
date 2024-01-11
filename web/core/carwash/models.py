from django.utils import timezone
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings
from decimal import Decimal
from django.core.validators import MinValueValidator
from core.account.models import Driver
from django.db import models
from core.base.models import VehicleInformation


class CarWashCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(
        upload_to='media/', null=True, blank=True)
    is_active = models.BooleanField(default=False)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        ordering = ["name"]
        verbose_name_plural = _("carwashcategories")

    def __str__(self):
        return self.name


class CarWashOrder(models.Model):
    category = models.ForeignKey(
        CarWashCategory, related_name="carwash", on_delete=models.CASCADE)
    car_type = models.ForeignKey(
        VehicleInformation, related_name='car_types', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    typeofcarwash = models.CharField(max_length=100)
    price = models.DecimalField(verbose_name=_(
        "price"), max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    delivery_address = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='media/', null=True, blank=True)
    description = models.TextField()
    arrivaltime = models.DateTimeField(default=timezone.now)

    def total_price(self):
        if self.category is not None:
            return self.quantity * self.price
        else:
            return 0

    def save(self, *args, **kwargs):
        if isinstance(self.car_type, str):
            vehicle_info = VehicleInformation.objects.filter(
                vehicle_type=self.car_type).first()
            if vehicle_info:
                self.car_type = vehicle_info
        super(CarWashOrder, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}'s Car Wash Order"
