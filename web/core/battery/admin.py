from django.contrib import admin
from core.battery.models import (
    BatteryBrand,
    Battery,
    BatteryCategory

)

admin.site.register(Battery),
admin.site.register(BatteryBrand),
admin.site.register(BatteryCategory),
