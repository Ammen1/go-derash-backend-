
from django.utils import timezone
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from decimal import Decimal
from mptt.models import MPTTModel, TreeForeignKey
from django.core.validators import MinValueValidator
from django.db import models
from core.base.models import VehicleInformation


class TyreCategory(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=False)
    description = models.TextField()
    price = models.DecimalField(verbose_name=_(
        "price"), max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    image = models.ImageField(
        upload_to='media/', null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        ordering = ["name"]
        verbose_name_plural = _("tyrescategory")

    def __str__(self):
        return self.name


class TyreBrand(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name_plural = _("brandes")

    def __str__(self):
        return self.name


class Tyre(models.Model):
    category = models.ForeignKey(
        TyreCategory, related_name='tyres', on_delete=models.CASCADE)
    car_type = models.ForeignKey(
        VehicleInformation, related_name='car_type', on_delete=models.CASCADE)
    brand = models.ForeignKey(
        TyreBrand, related_name="tyrebrandes", on_delete=models.CASCADE)
    tyre_size = models.CharField(max_length=100)
    tyre_type = models.CharField(max_length=100)
    qty = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    delivery_address = models.CharField(max_length=255)
    total_cost = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    arrivaltime = models.DateTimeField(default=timezone.now)

    def total_price(self):
        if self.category is not None:
            return self.qty * self.category.price
        else:
            return 0

    # def save(self, *args, **kwargs):
    #     if isinstance(self.car_type, str):
    #         vehicle_info = VehicleInformation.objects.filter(
    #             vehicle_type=self.car_type).first()
    #         if vehicle_info:
    #             self.car_type = vehicle_info
    #     super(Tyre, self).save(*args, **kwargs)

    # def __str__(self):
    #     return f"{self.tyre_type}'s Tyre Order"


# class Order(models.Model):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name='orders',
#         null=True,
#         blank=True
#     )
#     tyres = models.ManyToManyField(Tyre, related_name='orders')
#     total_price = models.DecimalField(
#         verbose_name=_("total price"),
#         max_digits=10,
#         decimal_places=2,
#         validators=[MinValueValidator(0)],
#         default=Decimal('0.00')
#     )
#     order_date = models.DateTimeField(default=timezone.now)


#     class Meta:
#         ordering = ['-order_date']
#         verbose_name_plural = _("orders")

#     def save(self, *args, **kwargs):
#         # Calculate total price based on the prices of individual tyres in the order
#         self.total_price = sum(tyre.total_price() for tyre in self.tyres.all())
#         super(Order, self).save(*args, **kwargs)
