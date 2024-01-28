from django.core.management.base import CommandError
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from core.engineoil.models import *
from core.base.models import VehicleInformation
from .serializers import *


# Engine Oil Views
from rest_framework import generics, status
from rest_framework.response import Response
from core.engineoil.serializers import EngineOilSerializer
from core.engineoil.models import EngineOilCategory, VehicleInformation, EngineBrand


class CreateEngineOil(generics.CreateAPIView):
    serializer_class = EngineOilSerializer

    def post(self, request, *args, **kwargs):
        # Create a mutable copy of request.data
        mutable_data = request.data.copy()

        serializer = self.get_serializer(data=mutable_data)

        if serializer.is_valid():
            category_name = serializer.validated_data.get("category")
            category, created = EngineOilCategory.objects.get_or_create(
                name=category_name)

            car_name = serializer.validated_data.get("car_type")
            car_type, created = VehicleInformation.objects.get_or_create(
                vehicle_model=car_name)

            brand_name = serializer.validated_data.get("brand")
            brand, created = EngineBrand.objects.get_or_create(name=brand_name)

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


class ListEngineOil(generics.ListAPIView):
    serializer_class = EngineOilSerializer
    queryset = EngineOil.objects.all()


class DetailEngineOil(generics.RetrieveAPIView):
    serializer_class = EngineOilSerializer
    queryset = EngineOil.objects.all()


class DeleteEgineOil(generics.DestroyAPIView):
    serializer_class = EngineOilSerializer
    queryset = EngineOil.objects.all()


class UpdateEngineOil(generics.UpdateAPIView):
    serializer_class = EngineOilSerializer
    queryset = EngineOil.objects.all()


# For EngineOilCategory views
class CreateEngineOilCategory(generics.CreateAPIView):
    serializer_class = EngineOilCategorySerializer
    queryset = EngineOilCategory.objects.all()


class ListEngineOilCategory(generics.ListAPIView):
    serializer_class = EngineOilCategorySerializer
    queryset = EngineOilCategory.objects.all()


class DetailEngineOilCategory(generics.RetrieveAPIView):
    serializer_class = EngineOilCategorySerializer
    queryset = EngineOilCategory.objects.all()


class DeleteEngineOilCategory(generics.DestroyAPIView):
    serializer_class = EngineOilCategorySerializer
    queryset = EngineOilCategory.objects.all()


class UpdateEngineOilCategory(generics.UpdateAPIView):
    serializer_class = EngineOilCategorySerializer
    queryset = EngineOilCategory.objects.all()


# For EngineOilBrand views
class CreateEngineOilBrand(generics.CreateAPIView):
    serializer_class = EngineOilBrandSerializer
    queryset = EngineBrand.objects.all()


class ListEngineOilBrand(generics.ListAPIView):
    serializer_class = EngineOilBrandSerializer
    queryset = EngineBrand.objects.all()


class DetailEngineOilBrand(generics.RetrieveAPIView):
    serializer_class = EngineOilBrandSerializer
    queryset = EngineBrand.objects.all()


class DeleteEngineOilBrand(generics.DestroyAPIView):
    serializer_class = EngineOilBrandSerializer
    queryset = EngineBrand.objects.all()


class UpdateEngineOilBrand(generics.UpdateAPIView):
    serializer_class = EngineOilBrandSerializer
    queryset = EngineBrand.objects.all()
