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
from rest_framework.generics import CreateAPIView


# Battery Views
class BatteryOrderView(CreateAPIView):
    serializer_class = BatteryOrderSerializer

    def post(self, request, *args, **kwargs):
        mutable_data = request.data.copy()
        serializer = self.get_serializer(data=mutable_data)
        if serializer.is_valid():
            category_name = serializer.validated_data.get("category")
            category, created = BatteryCategory.objects.get_or_create(
                name=category_name)
            car_name = serializer.validated_data.get("car_type")
            car_type, created = VehicleInformation.objects.get_or_create(
                vehicle_model=car_name)
            brand_name = serializer.validated_data.get("brand")
            brand, created = BatteryBrand.objects.get_or_create(
                name=brand_name)
            price_per_unit = category.price
            # Calculate total cost based on qty and price
            qty = serializer.validated_data.get("qty")
            total_cost = qty * price_per_unit

            # Update the serializer data with calculated total_cost
            serializer.validated_data["total_cost"] = total_cost

            serializer.validated_data["category"] = category
            serializer.validated_data["car_type"] = car_type
            serializer.validated_data["brand"] = brand

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print(serializer.errors)
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
    serializer_class = BatteryBrandSerializer
    queryset = BatteryBrand.objects.all()


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
    serializer_class = BatteryCategorySerializer
    queryset = BatteryCategory.objects.all()


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
