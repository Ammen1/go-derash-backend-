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


class FuelCategory(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(verbose_name=_(
        "price"), max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    description = models.TextField()
    image = models.ImageField(
        upload_to='media/', null=True, blank=True)
    is_active = models.BooleanField(default=False)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        ordering = ["name"]
        verbose_name_plural = _("fuelcategories")

    def __str__(self):
        return self.name


class FuelBrand(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name_plural = _("brandes")

    def __str__(self):
        return self.name


class GasLineDetails(models.Model):
    category = models.ForeignKey(
        FuelCategory, related_name='gaslines', on_delete=models.CASCADE)
    car_type = models.ForeignKey(
        VehicleInformation, on_delete=models.CASCADE)
    brand = models.ForeignKey(
        FuelBrand, related_name="brandes", on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    delivery_address = models.CharField(max_length=255)
    arrivaltime = models.DateTimeField(default=timezone.now)
    fuel_type = models.CharField(max_length=200, default=True)
    price = models.DecimalField(verbose_name=_(
        "price"), max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def total_price(self):
        if self.category is not None:
            return self.qty * self.price
        else:
            return 0

    def save(self, *args, **kwargs):
        if isinstance(self.car_type, str):
            vehicle_info = VehicleInformation.objects.filter(
                vehicle_type=self.car_type).first()
            if vehicle_info:
                self.car_type = vehicle_info
        super(GasLineDetails, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.fuel_capacity}L, {self.current_fuel_level}L"
