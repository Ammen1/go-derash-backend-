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
    total_price = serializers.SerializerMethodField()

    class Meta:
        models = EngineOil
        fields = '__all__'

    def get_total_price(self, obj):
        return obj.total_price()


class TyreSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Tyre
        fields = '__all__'

    def get_total_price(self, obj):
        return obj.total_price()


class GasLineDetailsSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = GasLineDetails
        fields = '__all__'

    def get_total_price(self, obj):
        return obj.total_price()


class CarWashSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CarWash
        fields = '__all__'

    def get_total_price(self, obj):
        return obj.total_price()


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
