from django.contrib import admin
from core.base.models import (
    VehicleInformation,
    Category,
    ServiceType,
    EngineOil,
    Tyre,
    CarWash,
    GasLineDetails,
    Subscription,
    Complaint,
    RouteManagement,
    Analysis,
    Brand

)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Analysis),
admin.site.register(ServiceType)
admin.site.register(EngineOil)
admin.site.register(Tyre)
admin.site.register(GasLineDetails)
admin.site.register(Subscription)
admin.site.register(Complaint)
admin.site.register(RouteManagement)
admin.site.register(VehicleInformation)
