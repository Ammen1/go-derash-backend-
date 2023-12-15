from rest_framework import serializers
from django.conf import settings
from rest_framework import serializers
from core.account.models import (
    NewUser,
    UserProfile,
    DriverProfile,
)


class CustomUserSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(required=True)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = NewUser
        fields = ('id', 'phone', 'password1', 'password2',
                  'is_active', 'is_superuser')
        extra_kwargs = {
            'password1': {'write_only': True},
            'password2': {'write_only': True}
        }

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                "Passwords must match...! Please try again...!")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password1')
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class DriverProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverProfile
        fields = ["driver", "address", "phone_number", "license_number"]


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        field = ["user", "location", "first_name", "last_name"]


class UserRegisterSerializer(serializers.ModelSerializer):

    phone = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('phone', "start_date", "is_staff", "is_active")
        extra_kwargs = {'password': {'write_only': True}}
