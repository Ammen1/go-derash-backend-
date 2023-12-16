from rest_framework import serializers
from django.conf import settings
from rest_framework import serializers
from core.account.models import (
    NewUser,
    AdminUser,
    Driver,
)


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ["driver", "address", "phone_number", "license_number"]


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    driverprofile = DriverSerializer(required=False)
    adminuser = AdminUserSerializer(required=False)

    class Meta:
        model = NewUser
        fields = ('id', 'phone', 'password1', 'password2',
                  'is_active', 'is_superuser', 'driverprofile', 'adminuser')
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
