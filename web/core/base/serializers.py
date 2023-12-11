from rest_framework import serializers
from django.conf import settings
from attr import attributes
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from models import (
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
        fields = ["name", "slug", "is_active"]
        read_only = True


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "slug", "description",
                  "category", "product_type", "price", "weight"]
        read_only = True
        editable = False


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ["name", ""]
        read_only = True
        editable = False


class ProductMediaSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ["img_url", "alt_text"]
        read_only = True
        editable = False

    def get_img_url(self, obj):
        return obj.img_url.url


class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('email', 'user_name', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}
