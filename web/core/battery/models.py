from django.utils import timezone
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from decimal import Decimal
from mptt.models import MPTTModel, TreeForeignKey
from django.core.validators import MinValueValidator
from core.account.models import Driver
from core.base.models import VehicleInformation


class BatteryCategory(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(verbose_name=_(
        "price"), max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    image = models.ImageField(
        upload_to='media/', null=True, blank=True)
    description = models.TextField(default="")
    is_active = models.BooleanField(default=False)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        ordering = ["name"]
        verbose_name_plural = _("batterycategories")

    def __str__(self):
        return self.name


class BatteryBrand(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = _("brandes")

    def __str__(self):
        return self.name


class Battery(models.Model):
    category = models.ForeignKey(
        BatteryCategory, related_name='batteries', on_delete=models.CASCADE, null=True)
    car_type = models.ForeignKey(VehicleInformation, on_delete=models.CASCADE)
    brand = models.ForeignKey(
        BatteryBrand, related_name='batterybrand', on_delete=models.CASCADE, null=False)
    select_battery_service = models.CharField(max_length=100)
    total_cost = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    qty = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    arrivaltime = models.DateTimeField(default=timezone.now)

    delivery_address = models.CharField(max_length=255)

    def total_price(self):
        if self.category is not None:
            return self.qty * self.category.price
        else:
            return 0

    def save(self, *args, **kwargs):
        if isinstance(self.car_type, str):
            vehicle_info = VehicleInformation.objects.filter(
                vehicle_type=self.car_type).first()
            if vehicle_info:
                self.car_type = vehicle_info

        super(Battery, self).save(*args, **kwargs)

    def __str__(self):
        return self.select_battery_service
