from django.contrib import admin
from .models import (
    # NewUser,
    # UserProfile,
    # Booking,
    VehicleInformation,
    Category,
    ServiceType,
    # BookingService,
    EngineOil,
    Tyre,
    CarWash,
    GasLineDetails,
    Subscription,
    # AutoCostCalculator,
    # Payment,
    # ReferralCoupon,
    # PushNotification,
    # # DriverProfile,
    # OrderAlert,
    EmergencyButtonAlert,
    AdminUser,
    Complaint,
    RouteManagement,

)
# admin.site.register(Booking)
# admin.site.register(NewUser)
# admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(ServiceType)
# admin.site.register(BookingService)
admin.site.register(EngineOil)
admin.site.register(Tyre)
admin.site.register(GasLineDetails)
admin.site.register(Subscription)
# admin.site.register(AutoCostCalculator)
# admin.site.register(Payment)
# admin.site.register(ReferralCoupon)
# admin.site.register(DriverProfile)
# admin.site.register(OrderAlert)
admin.site.register(EmergencyButtonAlert)
admin.site.register(AdminUser)
admin.site.register(Complaint)
admin.site.register(RouteManagement)
admin.site.register(VehicleInformation)
