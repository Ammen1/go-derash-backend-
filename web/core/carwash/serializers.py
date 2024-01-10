from rest_framework import serializers
from django.conf import settings
from attr import attributes
from django.core.exceptions import ObjectDoesNotExist
from core.base.models import VehicleInformation
from core.carwash.models import CarWashOrder
from rest_framework import serializers
from core.account.serializers import CustomUserSerializer


class CarWashOrderSerializer(serializers.ModelSerializer):
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model = CarWashOrder
        fields = ["id", "car_type", "name", "delivery_address", "typeofcarwash",
                  "quantity", "arrivaltime", "total_cost", "category", "image", ]

    def get_total_cost(self, obj):
        total_price = obj.total_price()

        total_cost = total_price * obj.quantity

        return total_cost

    def to_internal_value(self, data):
        # Convert 'car_type' from a string to the corresponding primary key
        if 'car_type' in data and isinstance(data['car_type'], str):
            vehicle_info = VehicleInformation.objects.filter(
                vehicle_type=data['car_type']).first()
            if vehicle_info:
                data['car_type'] = vehicle_info.pk

        return super().to_internal_value(data)
