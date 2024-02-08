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
        fields = '__all__'


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    driverprofile = DriverSerializer(required=False)
    adminuser = AdminUserSerializer(required=False)
    user = serializers.CharField(required=True)

    class Meta:
        model = NewUser
        fields = ('id', 'phone', "email", 'password1', 'password2',
                  'is_active', 'is_superuser', 'driverprofile', 'adminuser', "last_login",  "start_date", "is_staff", "is_admin_user", "is_driver", "address", "user_permissions")
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

    def to_internal_value(self, data):
        if 'user' in data and isinstance(data['user'], str):
            user_info = NewUser.objects.filter(
                user=data['user']['is_admin_user']).first()
            if user_info:
                data['user'] = user_info.pk

        return super().to_internal_value(data)
