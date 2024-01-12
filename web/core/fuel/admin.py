from django.contrib import admin
from core.fuel.models import (
    FuelCategory,
    FuelBrand,
    GasLineDetails,

)

admin.site.register(FuelCategory),
admin.site.register(FuelBrand),
admin.site.register(GasLineDetails),
