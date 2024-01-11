from django.contrib import admin
from core.base.models import (
    VehicleInformation,
    Category,
    Subscription,
    Complaint,
    RouteManagement,
    Analysis,


)

admin.site.register(Category)
admin.site.register(Analysis)
admin.site.register(Subscription)
admin.site.register(Complaint)
admin.site.register(RouteManagement)
admin.site.register(VehicleInformation)
