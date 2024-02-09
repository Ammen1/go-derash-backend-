from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):
    def create_superuser(
        self, phone, password, email=None, **other_fields
    ):
        if not (phone or email):
            raise ValueError(
                "Either the Phone or Email field must be set for the superuser.")

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must be assigned to is_superuser=True.")

        user = self.model(phone=phone, email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(null=True, blank=True)
    driver_photo = models.ImageField(
        upload_to='driver_photos/', null=True, blank=True, default="")
    address = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin_user = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = "phone"
    EMAIL_FIELD = "email"

    def __str__(self):
        if self.is_admin_user:
            is_admin_user = True
            return f"Admin User: {self.phone} - {self.email}"
        elif self.is_driver:
            return f"Driver: {self.phone} - {self.email}"
        else:
            return f"User: {self.phone} - {self.email} - Address: {self.address}"


class Driver(models.Model):
    user = models.OneToOneField(NewUser, on_delete=models.CASCADE, default="")
    address = models.CharField(max_length=255)
    license_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    vehicle_type = models.CharField(max_length=50, default="")
    vehicle_registration = models.CharField(max_length=20, default="")
    available_for_delivery = models.BooleanField(default=True)
    driver_photo = models.ImageField(
        upload_to='driver_photos/', null=True, blank=True)

    is_driver = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.phone} - {self.user.email}"

    def save(self, *args, **kwargs):
        if self.user and not self.user.is_admin_user:
            self.user.is_driver_user = True
            self.user.save()
        super(Driver, self).save(*args, **kwargs)


class AdminUser(models.Model):
    user = models.OneToOneField(
        NewUser, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_admin_user = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.phone} - {self.user.email}"

    def save(self, *args, **kwargs):
        if self.user and not self.user.is_admin_user:
            self.user.is_admin_user = True
            self.user.save()
        super(AdminUser, self).save(*args, **kwargs)


class Car(models.Model):
    user = models.OneToOneField(
        NewUser, null=True, on_delete=models.CASCADE)
    VIN = models.CharField(max_length=17, unique=True,
                           help_text="Vehicle Identification Number")
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=20)

    # International Requirements
    country_of_registration = models.CharField(
        max_length=50, blank=True, null=True, help_text="Country of registration")
    international_insurance_provider = models.CharField(
        max_length=50, blank=True, null=True, help_text="International insurance provider")
    registration_expiration_date = models.DateField(
        null=True, blank=True, help_text="Date of registration expiration")
    international_service_requirements = models.TextField(
        blank=True, null=True, help_text="International service requirements")

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.VIN})"
