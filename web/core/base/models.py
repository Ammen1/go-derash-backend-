from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class CustomAccountManager(BaseUserManager):
    def create_superuser(
        self, phone, password, **other_fields
    ):

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must be assigned to is_superuser=True.")

        return self.create_user(
            phone, password, **other_fields
        )

    def create_user(self, phone, password, **other_fields):
        if not phone:
            raise ValueError(_("You must provide an phone number"))

        user = self.model(
            phone=phone,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=15, blank=False, unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = "phone"

    def __str__(self):
        return self.full_name


class UserProfile(models.Model):
    user = models.OneToOneField(NewUser, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Booking(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    service_type = models.ForeignKey('ServiceType', on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    timestamp = models.DateField(auto_now_add=True)


class VehicleInformation(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=100)
    driver_license = models.CharField(max_length=100)


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class ServiceType(models.Model):
    location = models.CharField(max_length=100)
    car_type = models.ForeignKey(VehicleInformation, on_delete=models.CASCADE)
    arrival_date = models.DateField()
    arrival_time = models.TimeField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # services = models.ManyToManyField(Service, through='BookingService')


class BookingService(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    service = models.ForeignKey(ServiceType, on_delete=models.CASCADE)


class EngineOil(models.Model):
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    engine_oil_type = models.CharField(max_length=100,)
    engine_size = models.CharField(max_length=100)


class Tyre(models.Model):
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    trye_size = models.CharField(max_length=100)
    trye_type = models.CharField(max_length=100)


class CarWash(models.Model):
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    wash_type = models.CharField(max_length=255)
    exterior = models.BooleanField()
    interior = models.BooleanField()
    water = models.BooleanField()


class GasLineDetails(models.Model):
    service = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    fuel_capacity = models.DecimalField(max_digits=8, decimal_places=2)
    current_fuel_level = models.DecimalField(max_digits=8, decimal_places=2)


class Subscription(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)


class AutoCostCalculator(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    distance_travelled = models.DecimalField(max_digits=8, decimal_places=2)
    # service_used = models.ForeignKey(Service, on_delete=models.CASCADE)
    service_type_used = models.ForeignKey(
        ServiceType, on_delete=models.CASCADE)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)


class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)


# class Chat(models.Model):
#     sender = models.ForeignKey(
#         NewUser, on_delete=models.CASCADE, related_name='inappchat_receiver')
#     receiver = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name='receiver')
#     message = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)


class ReferralCoupon(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    coupon_code = models.CharField(max_length=20)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    expiry_date = models.DateField()


class PushNotification(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

# Driver App Models


class DriverProfile(models.Model):
    driver = models.OneToOneField(NewUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    license_number = models.CharField(max_length=20)


class OrderAlert(models.Model):
    driver = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)


# class InAppChat(models.Model):
#     sender = models.ForeignKey(NewUser, on_delete=models.CASCADE)
#     receiver = models.ForeignKey(NewUser, on_delete=models.CASCADE)
#     message = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)


class EmergencyButtonAlert(models.Model):
    driver = models.ForeignKey(NewUser, on_delete=models.CASCADE)
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
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)


class RouteManagement(models.Model):
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    distance = models.DecimalField(max_digits=8, decimal_places=2)
    estimated_time = models.TimeField()
