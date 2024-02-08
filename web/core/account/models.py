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
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin_user = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    address = models.CharField(max_length=255, null=True, blank=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = "phone"
    EMAIL_FIELD = "email"

    def __str__(self):
        if self.is_admin_user:
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


class AdminUser(models.Model):
    user = models.OneToOneField(
        NewUser, null=True, on_delete=models.CASCADE, default="")
    username = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_admin_user = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.phone} - {self.user.email}"
