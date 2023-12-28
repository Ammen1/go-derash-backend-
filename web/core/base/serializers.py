from .models import CarWashOrder
from rest_framework import serializers
from django.conf import settings
from attr import attributes
from django.core.exceptions import ObjectDoesNotExist
from core.base.models import *
from rest_framework import serializers
from core.account.serializers import CustomUserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# class ServiceTypeSerializer(serializers.ModelSerializer):
#     def get_total_cost(self, obj):
#         # Add your logic to calculate the total cost based on the obj
#         # For example, if obj has a field named 'price' and 'quantity':
#         return obj.total_cost * obj.quantity

#     class Meta:
#         model = ServiceType
#         fields = '__all__'


class VehicleInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleInformation
        fields = ["vehicle_type", "vehicle_model",
                  "license_plate", "driver_license"]
        read_only = False
        editable = True


class TyreSerializer(serializers.ModelSerializer):
    total_cost = serializers.SerializerMethodField()
    car_type = serializers.CharField(write_only=True)

    class Meta:
        model = Tyre
        fields = ["id", "category", "car_type", "arrivaltime", "total_cost",
                  "tyre_size", "tyre_type", "qty", "delivery_address"]

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


class BatteryOrderSerializer(serializers.ModelSerializer):
    total_cost = serializers.SerializerMethodField()
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


class CarWashOrderSerializer(serializers.ModelSerializer):
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model = CarWashOrder
        fields = ["id", "car_type", "name", "delivery_address", "typeofcarwash",
                  "quantity", "arrivaltime", "total_cost", "category",]

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


class EngineOilSerializer(serializers.ModelSerializer):
    total_cost = serializers.SerializerMethodField()
    car_type = serializers.CharField(write_only=True)

    class Meta:
        model = EngineOil
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


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ["user", "start_date", "end_date", "active"]


class ComplaintSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Complaint
        fields = '__all__'


class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = '__all__'
