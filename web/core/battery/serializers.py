from rest_framework import serializers
from django.conf import settings
from attr import attributes
from django.core.exceptions import ObjectDoesNotExist
from core.battery.models import *
from rest_framework import serializers
from core.base.models import VehicleInformation


class BatteryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BatteryCategory
        fields = '__all__'


class BatteryBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatteryBrand
        fields = '__all__'


class BatteryOrderSerializer(serializers.ModelSerializer):
    total_cost = serializers.SerializerMethodField()
    batteryBrand = serializers.CharField(write_only=True)
    car_type = serializers.CharField(write_only=True)

    class Meta:
        model = Battery
        fields = '__all__'

    def get_total_cost(self, obj):
        total_price = obj.total_price()
        total_cost = total_price * obj.qty
        return total_cost

    def to_internal_value(self, data):
        # Convert 'car_type' from a string to the corresponding primary key
        if 'car_type' in data and isinstance(data['car_type'], str):
            vehicle_info = VehicleInformation.objects.filter(
                vehicle_type=data['car_type']).first()
            if vehicle_info:
                data['car_type'] = vehicle_info.pk

        return super().to_internal_value(data)

    def to_internal_value(self, data):
        if 'batteryBrand' in data and isinstance(data['car_type'], str):
            batterybrand = BatteryBrand.objects.filter(
                name=data['name']).first()
        return super().to_internal_value(data)