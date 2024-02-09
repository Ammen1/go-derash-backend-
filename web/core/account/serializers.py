from rest_framework import serializers
from core.account.models import NewUser, AdminUser, Driver
from .models import Car


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    driverprofile = DriverSerializer(required=False)
    adminuser = AdminUserSerializer(required=False)

    class Meta:
        model = NewUser
        fields = ('id', 'phone', 'email', 'password1', 'password2',
                  'is_active', 'is_superuser', 'driverprofile', 'adminuser', 'last_login', 'start_date', 'is_staff', 'is_admin_user', 'is_driver', 'address', 'user_permissions')
        extra_kwargs = {
            'password1': {'write_only': True},
            'password2': {'write_only': True},
        }

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords must match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password2', None)
        password = validated_data.pop('password1', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
