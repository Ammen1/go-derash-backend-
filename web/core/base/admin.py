from django.contrib import admin
from .models import (
    NewUser,
    UserProfile,
    Booking,
    VehicleInformation,
    Service,
    ServiceType,
    BookingService,
    EngineOil,
    Tyre,
    CarWash,
    GasLineDetails,
    Subscription,
    AutoCostCalculator,
    Payment,
    ReferralCoupon,
    PushNotification,
    DriverProfile,
    OrderAlert,
    EmergencyButtonAlert,
    AdminUser,
    Complaint,
    RouteManagement,
)


@admin.register(NewUser)
class NewUserAdmin(admin.ModelAdmin):
    list_display = ('phone', 'start_date', 'is_staff', 'is_active')
    search_fields = ('phone', 'start_date')
    # Add more configuration as needed


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'first_name', 'last_name')
    search_fields = ('user__phone', 'location', 'first_name', 'last_name')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'service_type', 'status', 'timestamp')
    search_fields = ('user__phone', 'service_type__location', 'status')
    # Add more configuration as needed


@admin.register(RouteManagement)
class RouteManagementAdmin(admin.ModelAdmin):
    list_display = ('start_location', 'end_location',
                    'distance', 'estimated_time')
    search_fields = ('start_location', 'end_location')
