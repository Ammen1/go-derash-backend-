from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from core.fuel.models import *
from core.account.serializers import CustomUserSerializer
from core.base.models import VehicleInformation


class FuelCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = FuelCategory
        fields = '__all__'


class FuelBrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = FuelBrand
        fields = '__all__'


class GasLineDetailsSerializer(serializers.ModelSerializer):
    total_cost = serializers.SerializerMethodField()
    car_type = serializers.CharField(write_only=True)
    brand = serializers.CharField(write_only=True)

    class Meta:
        model = GasLineDetails
        fields = '__all__'

    def get_total_cost(self, obj):
        total_price = obj.total_price()
        total_cost = total_price * obj.qty
        return total_cost

    def to_internal_value(self, data):
        if 'car_type' in data and isinstance(data['car_type'], str):
            vehicle_info = VehicleInformation.objects.filter(
                vehicle_type=data['car_type']).first()
            if vehicle_info:
                data['car_type'] = vehicle_info.pk

        return super().to_internal_value(data)

    def to_internal_value(self, data):
        if 'brand' in data and isinstance(data['brand'], str):
            brand = FuelBrand.objects.filter(name=data['brand']).first()

            if brand:
                data['brand'] = brand.pk
        return super().to_internal_value(data)
