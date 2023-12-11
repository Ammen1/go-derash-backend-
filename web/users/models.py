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
