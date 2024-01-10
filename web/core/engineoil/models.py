from django.utils import timezone
from django.core.exceptions import ValidationError
from django.conf import settings
from decimal import Decimal
from django.core.validators import MinValueValidator
from core.account.models import Driver
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from core.base.models import VehicleInformation
from django.utils.translation import gettext_lazy as _


class EngineOilCategory(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=False)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        ordering = ["name"]
        verbose_name_plural = _("enginecategories")

    def __str__(self):
        return self.name


class EngineBrand(models.Model):
    name = models.CharField(max_length=100,)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = _("enginebrandes")

    def __str__(self):
        return self.name


class EngineOil(models.Model):
    category = models.ForeignKey(
        EngineOilCategory, related_name='oilengine', on_delete=models.CASCADE)
    car_type = models.ForeignKey(
        VehicleInformation, on_delete=models.CASCADE)
    enginebrand = models.ForeignKey(
        EngineBrand, related_name="enginebrand", on_delete=models.CASCADE)
    engine_oil_type = models.CharField(max_length=100)
    engine_size = models.CharField(max_length=100)
    qty = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    delivery_address = models.CharField(max_length=255)
    price = models.DecimalField(verbose_name=_(
        "price"), max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    image = models.ImageField(
        upload_to='media/', null=True, blank=True)
    description = models.TextField()
    arrivaltime = models.DateTimeField(default=timezone.now)

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
        super(EngineOil, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.engine_oil_type}'s Tyre Order"
