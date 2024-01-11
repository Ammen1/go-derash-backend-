from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from core.tyre.models import *
from core.account.serializers import CustomUserSerializer


class TyreCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TyreCategory
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class TyreSerializer(serializers.ModelSerializer):
    total_cost = serializers.SerializerMethodField()
    car_type = serializers.CharField(write_only=True)

    class Meta:
        model = Tyre
        fields = '__all__'

    def get_total_cost(self, obj):
        total_price = obj.total_price()
        total_cost = total_price * obj.qty

        return total_cost

    def to_internal_value(self, data):
        if 'car_type' in data and isinstance(data['car_type'], str):
            # Assuming VehicleInformation model has a field named 'vehicle_type'
            vehicle_info = VehicleInformation.objects.filter(
                vehicle_type=data['car_type']).first()
            if vehicle_info:
                data['car_type'] = vehicle_info.pk

        return super().to_internal_value(data)
