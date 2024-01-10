from django.core.management.base import CommandError
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from core.battery.models import *
from .serializers import *


# Battery Views
class BatteryOrderView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer = BatteryOrderSerializer(data=request.data)
        if serializer.is_valid():

            category_name = serializer.validated_data.get("category")
            category, created = Category.objects.get_or_create(
                name=category_name)

            car_name = serializer.validated_data.get("car_type")
            car_type, created = VehicleInformation.objects.get_or_create(
                vehicle_model=car_name)

            serializer.validated_data["category"] = category
            serializer.validated_data['car_type'] = car_type

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Debugging: Print serializer.errors to inspect the validation errors
        print("Validation Errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
