from django.contrib import admin
from core.base.models import (
    VehicleInformation,
    Category,
    EngineOil,
    Tyre,
    CarWashOrder,
    GasLineDetails,
    Subscription,
    Complaint,
    RouteManagement,
    Analysis,
    Battery

)
admin.site.register(Battery)
admin.site.register(Category)
admin.site.register(Analysis),
admin.site.register(EngineOil)
admin.site.register(Tyre)
admin.site.register(GasLineDetails)
admin.site.register(Subscription)
admin.site.register(Complaint)
admin.site.register(RouteManagement)
admin.site.register(VehicleInformation)
admin.site.register(CarWashOrder)
