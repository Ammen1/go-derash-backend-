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


# Fuel Views
class FuelOrderCreateView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer = GasLineDetailsSerializer(data=request.data)
        if serializer.is_valid():
            # Get or create a Category instance based on your logic
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
