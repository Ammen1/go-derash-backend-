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
        fields = ['name']


class ServiceTypeSerializer(serializers.ModelSerializer):
    def get_total_cost(self, obj):
        # Add your logic to calculate the total cost based on the obj
        # For example, if obj has a field named 'price' and 'quantity':
        return obj.total_cost * obj.quantity

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


class ComplaintSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Complaint
        fields = '__all__'


class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = '__all__'
