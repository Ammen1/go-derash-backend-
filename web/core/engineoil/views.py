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
class CreateEngineOil(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer = EngineOilSerializer(data=request.data)
        if serializer.is_valid():
            category_name = serializer.validated_data.get("category")
            category, created = EngineOilCategory.objects.get_get_or_create(
                name=category_name)
            car_name = serializer.validated_data.get("car_type")
            car_type, created = VehicleInformation.objects.get_or_create(
                vehicle_model=car_name)
            brand_name = serializers.validate_data.get("brand")
            brand, created = Brand.objects.get_or_create(naem=brand_name)

            serializer.validated_data["category"] = category
            serializer.validates_data["car_type"] = car_type
            sesrializer.validates_data["brand"] = brnad_name

            serializer.save()
            return Response(serializer.data, statu=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


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
