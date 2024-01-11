from django.contrib import admin

from core.carwash.models import (
    CarWashOrder,
    CarWashCategory
)
admin.site.register(CarWashOrder)
admin.site.register(CarWashCategory)
