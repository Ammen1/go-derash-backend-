from django.contrib import admin
from core.engineoil.models import (
    EngineOilCategory,
    EngineBrand,
    EngineOil

)

admin.site.register(EngineOilCategory),
admin.site.register(EngineBrand),
admin.site.register(EngineOil),
