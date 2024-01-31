from django.core.management.base import CommandError
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from core.carwash.models import *
from .serializers import *


# Carwash Views
class CarWashOrderCreateView(generics.CreateAPIView):
    serializer_class = CarWashOrderSerializer

    def post(self, request, *args, **kwargs):
        mutable_data = request.data.copy()
        serializer = self.get_serializer(data=mutable_data)
        serializer = CarWashOrderSerializer(data=request.data)
        if serializer.is_valid():
            category_name = serializer.validated_data.get("category")
            category, created = CarWashCategory.objects.get_or_create(
                name=category_name)
            car_name = serializer.validated_data.get("car_type")
            car_type, created = VehicleInformation.objects.get_or_create(
                vehicle_model=car_name)
            qty = serializer.validated_data.get("qty")
            price_per_unit = category.price
            total_cost = qty*price_per_unit

            serializer.validated_data["total_cost"] = total_cost

            serializer.validated_data["category"] = category
            serializer.validated_data['car_type'] = car_type

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarWashOrderListView(generics.ListAPIView):
    serializer_class = CarWashOrderSerializer
    queryset = CarWashOrder.objects.all()


class DeleteCarWash(generics.DestroyAPIView):
    serializer_class = CarWashOrderSerializer
    queryset = CarWashOrder.objects.all()


class DetailCarWash(generics.RetrieveAPIView):
    serializer_class = CarWashOrderSerializer
    queryset = CarWashOrder.objects.all()


class EditCarWash(generics.UpdateAPIView):
    serializer_class = CarWashOrderSerializer
    queryset = CarWashOrder.objects.all()


# Carwash Views
class CreateCategory(generics.CreateAPIView):
    serializer_class = CarWashCategorySerializer
    queryset = CarWashCategory.objects.all()


class ListCategory(generics.ListAPIView):
    serializer_class = CarWashCategorySerializer
    queryset = CarWashCategory.objects.all()


class DetailCategory(generics.RetrieveAPIView):
    serializer_class = CarWashCategorySerializer
    queryset = CarWashCategory.objects.all()


class DeleteCategory(generics.DestroyAPIView):
    serializer_class = CarWashCategorySerializer
    queryset = CarWashCategory.objects.all()


class UpdateCategory(generics.UpdateAPIView):
    serializer_class = CarWashCategorySerializer
    queryset = CarWashCategory.objects.all()
