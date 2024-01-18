from django.core.management.base import CommandError
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from core.fuel.models import *
from .serializers import *
from core.base.models import VehicleInformation


# Fuel Views
class FuelOrderCreateView(generics.CreateAPIView):
    serializer_class = GasLineDetailsSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            category_name = serializer.validated_data.get("category")
            category, created = FuelCategory.objects.get_or_create(
                name=category_name)

            car_name = serializer.validated_data.get("car_type")
            car_type, created = VehicleInformation.objects.get_or_create(
                vehicle_model=car_name)

            brand_name = serializer.validated_data.get("brand")
            brand, created = FuelBrand.objects.get_or_create(name=brand_name)

            # Assuming you have a price field in TyreCategory model
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


class ListFuel(generics.ListAPIView):
    serializer_class = GasLineDetailsSerializer
    queryset = GasLineDetails.objects.all()


class DetailGasline(generics.RetrieveAPIView):
    serializer_class = GasLineDetailsSerializer
    queryset = GasLineDetails.objects.all()


class DeleteGasline(generics.DestroyAPIView):
    serializer_class = GasLineDetailsSerializer
    queryset = GasLineDetails.objects.all()


class UpdateGasline(generics.UpdateAPIView):
    serializer_class = GasLineDetailsSerializer
    queryset = GasLineDetails.objects.all()


# views for Category
class CreateFuelCategory(generics.CreateAPIView):
    serializer_class = FuelCategorySerializer
    queryset = FuelCategory.objects.all()


class ListFuelCategory(generics.ListAPIView):
    serializer_class = FuelCategorySerializer
    queryset = FuelCategory.objects.all()


class DetailFuelCategory(generics.RetrieveAPIView):
    serializer_class = FuelCategorySerializer
    queryset = FuelCategory.objects.all()


class DeleteFuelCategory(generics.DestroyAPIView):
    serializer_class = FuelCategorySerializer
    queryset = FuelCategory.objects.all()


class UpdateFuelCategory(generics.UpdateAPIView):
    serializer_class = FuelCategorySerializer
    queryset = FuelCategory.objects.all()


# views for FuelBrand
class CreateFuelBrand(generics.CreateAPIView):
    serializer_class = FuelBrandSerializer
    queryset = FuelBrand.objects.all()


class ListFuelBrand(generics.ListAPIView):
    serializer_class = FuelBrandSerializer
    queryset = FuelBrand.objects.all()


class DetailFuelBrand(generics.RetrieveAPIView):
    serializer_class = FuelBrandSerializer
    queryset = FuelBrand.objects.all()


class DeleteFuelBrand(generics.DestroyAPIView):
    serializer_class = FuelBrandSerializer
    queryset = FuelBrand.objects.all()


class UpdateFuelBrand(generics.UpdateAPIView):
    serializer_class = FuelBrandSerializer
    queryset = FuelBrand.objects.all()
