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
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy as _


class Category(MPTTModel):
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
        verbose_name_plural = _("services")

    def __str__(self):
        return self.name


class BaseService(models.Model):
    service_type = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='base_services'
    )

    class Meta:
        abstract = True

    def calculate_total_cost(self):
        return self.service_type.regular_price


class VehicleInformation(models.Model):
    vehicle_type = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=100)
    driver_license = models.CharField(max_length=100)

    def __str__(self):
        return self.vehicle_type


class Tyre(models.Model):
    category = models.ForeignKey(
        Category, related_name='tyres', on_delete=models.CASCADE)
    car_type = models.ForeignKey(
        VehicleInformation, related_name='car_type', on_delete=models.CASCADE)
    tyre_size = models.CharField(max_length=100)
    tyre_type = models.CharField(max_length=100)
    qty = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    delivery_address = models.CharField(max_length=255)
    arrivaltime = models.DateTimeField(default=timezone.now)

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
        super(Tyre, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.tyre_type}'s Tyre Order"


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)

    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError(
                _('End date should be greater than or equal to start date'))

        if self.end_date <= timezone.now().date():
            raise ValidationError(_('End date should be in the future'))

    def __str__(self):
        return f"{self.start_date} to {self.end_date}"


# Web Admin Models
class Complaint(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)


class RouteManagement(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    distance = models.DecimalField(max_digits=8, decimal_places=2)
    estimated_time = models.TimeField()


class Analysis(models.Model):
    date = models.DateField()
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2)
    total_fuel_consumption = models.DecimalField(
        max_digits=8, decimal_places=2)
    total_distance_covered = models.DecimalField(
        max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Analysis for {self.date}"
