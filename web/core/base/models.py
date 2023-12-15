from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from decimal import Decimal
from mptt.models import MPTTModel, TreeForeignKey
from django.core.validators import MinValueValidator


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
    description = models.TextField()
    category = models.ForeignKey(
        Category, related_name="service_types", on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, related_name="service_types",
                              on_delete=models.SET_NULL, blank=True, null=True)
    total_cost = models.DecimalField(verbose_name=_(
        "total price"), max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def create_service_instance(self):
        if self.select_battery_service:
            return BatteryService(self)
        elif self.engine_oils.exists():
            return EngineOilService(self)
        elif self.tyres.exists():
            return TyreService(self)
        elif self.carwashes.exists():
            return CarWashService(self)
        elif self.gaslines.exists():
            return GasLineService(self)
        else:
            return BaseService(self)

    def __str__(self):
        return self.location


class BaseService(models.Model):
    service_type = models.ForeignKey(
        ServiceType, on_delete=models.CASCADE, related_name='base_services'
    )

    class Meta:
        abstract = True

    def calculate_total_cost(self):
        return self.service_type.regular_price


class VehicleInformation(models.Model):
    service_type = models.ForeignKey(
        ServiceType, related_name='vehicles', on_delete=models.PROTECT)
    vehicle_type = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=100)
    driver_license = models.CharField(max_length=100)

    def __str__(self):
        return self.vehicle_type


class Battery(models.Model):
    car_type = models.ForeignKey(
        VehicleInformation, on_delete=models.CASCADE)
    service_type = models.ForeignKey(
        ServiceType, related_name='batteries', on_delete=models.PROTECT)
    brand = models.ForeignKey(
        Brand, related_name='batteries', on_delete=models.CASCADE)
    select_battery_service = models.CharField(max_length=100, choices=[
        ('standard', 'Standard'), ('premium', 'Premium'), ('agm', 'AGM')])
    regular_price = models.DecimalField(verbose_name=_(
        "Regular price"), max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    qty = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def total_price(self):
        return self.qty * self.regular_price

    def __str__(self):
        return self.select_battery_service


class EngineOil(models.Model):
    car_type = models.ForeignKey(
        VehicleInformation, on_delete=models.CASCADE)
    service_type = models.ForeignKey(
        ServiceType, related_name='engine_oils', on_delete=models.PROTECT)
    brand = models.ForeignKey(
        Brand, related_name='engine_oils', on_delete=models.CASCADE)
    engine_oil_type = models.CharField(max_length=100)
    engine_size = models.CharField(max_length=100)
    regular_price = models.DecimalField(verbose_name=_(
        "Regular price"), max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    qty = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def total_price(self):
        return self.qty * self.regular_price

    def __str__(self):
        return self.engine_oil_type


class Tyre(models.Model):
    service_type = models.ForeignKey(
        ServiceType, related_name='tyes', on_delete=models.PROTECT)
    car_type = models.ForeignKey(
        VehicleInformation, on_delete=models.CASCADE)
    tyre_size = models.CharField(max_length=100)
    tyre_type = models.CharField(max_length=100)
    regular_price = models.DecimalField(verbose_name=_(
        "Regular price"), max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    qty = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def total_price(self):
        return self.qty * self.regular_price

    def __str__(self):
        return self.tyre_type


class CarWash(models.Model):
    car_type = models.ForeignKey(
        VehicleInformation, on_delete=models.CASCADE)
    service_type = models.ForeignKey(
        ServiceType, related_name='carwashes', on_delete=models.PROTECT)
    wash_type = models.CharField(max_length=255)
    exterior = models.BooleanField()
    interior = models.BooleanField()
    water = models.BooleanField()
    regular_price = models.DecimalField(verbose_name=_(
        "Regular price"), max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    qty = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def total_price(self):
        return self.qty * self.regular_price

    def __str__(self):
        return self.wash_type


class GasLineDetails(models.Model):
    car_type = models.ForeignKey(
        VehicleInformation, on_delete=models.CASCADE)
    service_type = models.ForeignKey(
        ServiceType, related_name='gaslines', on_delete=models.PROTECT)
    fuel_capacity = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text='Fuel capacity in liters'
    )
    current_fuel_level = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text='Current fuel level in liters'
    )
    regular_price = models.DecimalField(verbose_name=_(
        "Regular price"), max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    qty = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def total_price(self):
        return self.qty * self.regular_price

    def clean(self):
        if self.fuel_capacity < self.current_fuel_level:
            raise ValidationError(
                _('Fuel capacity should be greater than or equal to current fuel level'))

    def __str__(self):
        return f"{self.fuel_capacity}L, {self.current_fuel_level}L"


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
