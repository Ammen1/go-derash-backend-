from django.contrib import admin
from core.account.models import (
    NewUser,
    AdminUser,
    Driver,
)
admin.site.register(Driver)
admin.site.register(NewUser)
admin.site.register(AdminUser)
