from rest_framework import serializers
from django.conf import settings
from attr import attributes
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from core.base.models import (
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
from rest_framework import serializers


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["name"]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["user", "service_type", "status"]
        read_only = False
        editable = True


class VehicleInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleInformation
        fields = ["vehicle_type", "vehicle_model",
                  "license_plate", "driver_license"]
        read_only = False
        editable = True


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ["location", "car_type", "arrival_date",
                  "arrival_time", "description", "price", "services"]


class BookingServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingService
        fields = ["booking", "service"]


class EngineOilSerializer(serializers.ModelSerializer):
    class Meta:
        models = EngineOil
        fields = ["service_type", "trye_size", "trye_type"]


class CarWashSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarWash
        field = ["service_type", "wash_type", "exterior", "interior", "water"]


class GasLineDetails(serializers.ModelSerializer):
    class Meta:
        model = GasLineDetails
        field = ["service", "fuel_capacity", "current_fuel_level"]


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        field = ["user", "start_date", "end_date", "active"]


class AutoCostCalculatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        field = ["booking", "distace_travelled",
                 "service_type_used", "total_cost"]


class DriverProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverProfile
        field = ["driver", "address", "phone_number", "license_number"]


class OrderAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderAlert
        field = ["driver", "booking", "timestamp", "status"]


class EmergencyButtonAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyButtonAlert
        field = ["driver", "timestamp", "location"]


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        field = ["user", "message", "timestamp", "status"]


class RouteManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteManagement
        field = ["start_location", "end_location",
                 "distance", "estimated_time"]


class UserRegisterSerializer(serializers.ModelSerializer):

    phone = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('phone', "start_date", "is_staff", "is_active")
        extra_kwargs = {'password': {'write_only': True}}


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        field = ["user", "location", "first_name", "last_name"]


class TyreSerializer(serializers.ModelSerializer):
    class Meta:
        models = Tyre
        field = ["service_type", "tyre_size", "tyre_type"]


class GasLineDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        models = GasLineDetails
        fields = ["service", "fuel_capacity", "current_fuel_level"]
