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
from core.orders.models import Order


class FuelCategory(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL)
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
    brand = models.ForeignKey(
        FuelBrand, related_name="brandes", on_delete=models.CASCADE)
    title = models.CharField(
        verbose_name=_("title"),
        help_text=_("Required"),
        max_length=255,
        default="",
    )
    slug = models.SlugField(max_length=255,  default="")
    fuel_type = models.CharField(max_length=200, default=True)
    image = models.ImageField(
        upload_to='tyre_images/', null=True, blank=True)
    regular_price = models.DecimalField(
        verbose_name=_("Regular price"),
        help_text=_("Maximum 999999.99"),
        error_messages={
            "max_digits": {
                "max_length": _("The price must be between 0 and 999999.99."),
            },
        },
        max_digits=8,
        decimal_places=2,
        default=0
    )

    discount_price = models.DecimalField(
        verbose_name=_("Discount price"),
        help_text=_("Maximum 999999.99"),
        error_messages={
            "max_digits": {
                "max_length": _("The price must be between 0 and 999999.99."),
            },
        },
        max_digits=8,
        decimal_places=2,
        default=0
    )
    is_active = models.BooleanField(
        verbose_name=_("Product visibility"),
        help_text=_("Change product visibility"),
        default=True,
    )
    created_at = models.DateTimeField(
        _("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return title


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name="item", on_delete=models.CASCADE)
    product = models.ForeignKey(
        GasLineDetails, related_name="order_items", on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
