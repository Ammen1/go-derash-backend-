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
        self, email, full_name, phone, password, **other_fields
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
            email, full_name, phone, password, **other_fields
        )

    def create_user(self, email, full_name, phone, password, **other_fields):

        if not email:
            raise ValueError(_("You must provide an email address"))
        if not phone:
            raise ValueError(_("You must provide an phone number"))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            full_name=full_name,
            phone=phone,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_("email address"), unique=True)
    full_name = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=15, blank=False)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone", "full_name"]

    def __str__(self):
        return self.full_name


class Driver(models.Model):
    user = models.OneToOneField(NewUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
