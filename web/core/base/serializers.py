from rest_framework import serializers
from django.conf import settings
from attr import attributes
from django.core.exceptions import ObjectDoesNotExist
from core.base.models import (
    Brand,
    VehicleInformation,
    Category,
    ServiceType,
    EngineOil,
    Tyre,
    CarWash,
    GasLineDetails,
    Subscription,
    EmergencyButtonAlert,
    AdminUser,
    Complaint,
    RouteManagement,
)
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ServiceTypeSerializer(serializers.ModelSerializer):
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model = ServiceType
        fields = '__all__'

    def get_total_cost(self, obj):
        service_instance = obj.create_service_instance()
        return service_instance.calculate_total_cost()


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]
        read_only = False
        editable = True


class VehicleInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleInformation
        fields = ["vehicle_type", "vehicle_model",
                  "license_plate", "driver_license"]
        read_only = False
        editable = True


class EngineOilSerializer(serializers.ModelSerializer):
    class Meta:
        models = EngineOil
        fields = ["service_type", "trye_size",
                  "trye_type", "regular_price", "qty"]


class CarWashSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarWash
        fields = ["service_type", "wash_type", "exterior",
                  "interior", "water", "regular_price", "qty"]


class GasLineDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasLineDetails
        fields = ["service", "fuel_capacity",
                  "current_fuel_level", "regular_price", "qty"]


class TyreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tyre  # Specify the model associated with this serializer
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ["user", "start_date", "end_date", "active"]


class EmergencyButtonAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyButtonAlert
        fields = ["driver", "timestamp", "location"]


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ["user", "message", "timestamp", "status"]


class RouteManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteManagement
        fields = ["start_location", "end_location",
                  "distance", "estimated_time"]


class TyreSerializer(serializers.ModelSerializer):
    class Meta:
        models = Tyre
        field = ["service_type", "tyre_size", "tyre_type"]


class GasLineDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        models = GasLineDetails
        fields = ["service", "fuel_capacity", "current_fuel_level"]
