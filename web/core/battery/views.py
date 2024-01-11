from django.core.management.base import CommandError
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from core.battery.models import *
from core.base.models import VehicleInformation
from .serializers import *


# Battery Views
class BatteryOrderView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer = BatteryOrderSerializer(data=request.data)
        if serializer.is_valid():

            category_name = serializer.validated_data.get("category")
            category, created = BatteryCategory.objects.get_or_create(
                name=category_name)

            car_name = serializer.validated_data.get("car_type")
            car_type, created = VehicleInformation.objects.get_or_create(
                vehicle_model=car_name)
            brand_name = serializers.validate_data.get("brand")
            brand, created = Brand.objects.get_or_create(naem=brand_name)

            serializer.validated_data["category"] = category
            serializer.validated_data['car_type'] = car_type
            sesrializer.validates_data["brand"] = brnad_name

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Debugging: Print serializer.errors to inspect the validation errors
        print("Validation Errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListBattery(generics.ListAPIView):
    serializer_class = BatteryOrderSerializer
    queryset = BatteryBrand.objects.all()


class DetailBattery(generics.RetrieveAPIView):
    serializer_class = BatteryBrandSerializer
    queryset = BatteryBrand.objects.all()


class DeleteBattery(generics.DestroyAPIView):
    serializer_class = BatteryBrandSerializer
    queryset = BatteryBrand.objects.all()


class UpdateBattery(generics.UpdateAPIView):
    serializer_class = BatteryBrandSerializer
    queryset = BatteryBrand.objects.all()


# BatteryBrand Views
class CreatBrand(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer = BatteryBrandSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print("Validation Errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListBrand(generics.ListAPIView):
    serializer_class = BatteryBrandSerializer
    queryset = BatteryBrand.objects.all()


class DeleteBrand(generics.DestroyAPIView):
    serializer_class = BatteryBrandSerializer
    queryset = BatteryBrand.objects.all()


class UpdateBrand(generics.UpdateAPIView):
    serializer_class = BatteryBrandSerializer
    queryset = BatteryBrand.objects.all()


class DetailBrand(generics.RetrieveAPIView):
    serializer_class = BatteryBrandSerializer
    queryset = BatteryBrand.objects.all()


# BatteryCategory Views
class CreatBatteryCategory(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer = BatteryCategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print("Validation Errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListBatteryCategory(generics.ListAPIView):
    serializer_class = BatteryCategorySerializer
    queryset = BatteryCategory.objects.all()


class DeleteBatteryCategory(generics.DestroyAPIView):
    serializer_class = BatteryCategorySerializer
    queryset = BatteryCategory.objects.all()


class UpdateBatteryCategory (generics.UpdateAPIView):
    serializer_class = BatteryCategorySerializer
    queryset = BatteryCategory.objects.all()


class DetailBatteryCategory(generics.RetrieveAPIView):
    serializer_class = BatteryCategorySerializer
    queryset = BatteryCategory.objects.all()
