from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from core.fuel.models import GasLineDetails, VehicleInformation
from core.account.serializers import CustomUserSerializer


class GasLineDetailsSerializer(serializers.ModelSerializer):
    total_cost = serializers.SerializerMethodField()
    car_type = serializers.CharField(write_only=True)

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
