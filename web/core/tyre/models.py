from django.utils import timezone
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from decimal import Decimal
from mptt.models import MPTTModel, TreeForeignKey
from django.core.validators import MinValueValidator
from django.db import models
from core.orders.models import Order


class TyreCategory(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=False)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        ordering = ["name"]
        verbose_name_plural = _("tyre categories")

    def __str__(self):
        return self.name


class TyreBrand(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name_plural = _("brands")

    def __str__(self):
        return self.name


class Tyre(models.Model):
    category = models.ForeignKey(
        TyreCategory, related_name='tyres', on_delete=models.CASCADE)
    title = models.CharField(
        verbose_name=_("title"),
        help_text=_("Required"),
        max_length=255,
        default="",
    )
    slug = models.SlugField(max_length=255,  default="")
    brand = models.ForeignKey(
        TyreBrand, related_name="tyre_brands", on_delete=models.CASCADE)
    tyre_size = models.CharField(max_length=100)
    tyre_type = models.CharField(max_length=100)
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
        return self.title
