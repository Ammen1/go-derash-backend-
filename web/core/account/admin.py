from django.contrib import admin
from .models import (
    NewUser,
    UserProfile,
    DriverProfile,
)
admin.site.register(DriverProfile)
admin.site.register(NewUser)
admin.site.register(UserProfile)
