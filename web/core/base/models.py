from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from decimal import Decimal
from django.core.validators import MinValueValidator
from mptt.models import MPTTModel, TreeForeignKey
from core.basket.services import BaseService, BatteryService, EngineOilService


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    is_active = models.BooleanField(default=False)
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        db_index=True,
        on_delete=models.CASCADE
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        ordering = ["name"]
        verbose_name_plural = _("services")

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ServiceType(models.Model):
    location = models.CharField(max_length=100)
    car_type = models.ForeignKey(
        'VehicleInformation', on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ForeignKey(
        Category, related_name="service_types", on_delete=models.PROTECT)
    regular_price = models.DecimalField(verbose_name=_(
        "Regular price"), max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(verbose_name=_(
        "Discount price"), max_digits=5, decimal_places=2)
    brand = models.ForeignKey(Brand, related_name="service_types",
                              on_delete=models.SET_NULL, blank=True, null=True)

    def create_service_instance(self):
        # Use Factory Pattern to create the appropriate service instance
        if self.select_battery_service:
            return BatteryService(self)
        elif self.engine_oils.exists():
            return EngineOilService(self)
        elif self.TryeService.exits():
            return TyreService(self)
        elif self.CarWashService.exit():
            return CarWashService(self)
        elif self.GasLineService.exit():
            return GasLineService(self)
        else:
            return BaseService(self)


class VehicleInformation(models.Model):
    vehicle_type = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=100)
    driver_license = models.CharField(max_length=100)


class Battery(models.Model):
    service_type = models.ForeignKey(
        ServiceType, related_name='batteries', on_delete=models.PROTECT)
    brand = models.ForeignKey(
        Brand, related_name='batteries', on_delete=models.CASCADE)
    select_battery_service = models.CharField(max_length=100, choices=[(
        'standard', 'Standard'), ('premium', 'Premium'), ('agm', 'AGM')])


class EngineOil(models.Model):
    service_type = models.ForeignKey(
        ServiceType, related_name='engine_oils', on_delete=models.PROTECT)
    brand = models.ForeignKey(
        Brand, related_name='engine_oils', on_delete=models.CASCADE)
    engine_oil_type = models.CharField(max_length=100)
    engine_size = models.CharField(max_length=100)


class Tyre(models.Model):
    service_type = models.ForeignKey(
        ServiceType, related_name='tyres', on_delete=models.PROTECT)
    brand = models.ForeignKey(
        Brand, related_name='tyres', on_delete=models.PROTECT)
    tyre_size = models.CharField(max_length=100)
    tyre_type = models.CharField(max_length=100)


class CarWash(models.Model):
    service_type = models.ForeignKey(
        ServiceType, related_name='car_washes', on_delete=models.PROTECT)
    wash_type = models.CharField(max_length=255)
    exterior = models.BooleanField()
    interior = models.BooleanField()
    water = models.BooleanField()


class GasLineDetails(models.Model):
    service_type = models.ForeignKey(
        ServiceType, related_name='gas_lines', on_delete=models.PROTECT)
    fuel_capacity = models.DecimalField(max_digits=8, decimal_places=2)
    current_fuel_level = models.DecimalField(max_digits=8, decimal_places=2)


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)


class EmergencyButtonAlert(models.Model):
    driver = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255)

# Web Admin Models


class AdminUser(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Complaint(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)


class RouteManagement(models.Model):
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    distance = models.DecimalField(max_digits=8, decimal_places=2)
    estimated_time = models.TimeField()
