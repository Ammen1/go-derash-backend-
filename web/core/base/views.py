from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from core.base.models import *
from .serializers import *


# Service Views
class CreateCategory(APIView):
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ServiceDetail(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class EditService(generics.UpdateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class DeleteService(generics.RetrieveDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


# Vehicle Information Views
class CreateVehicleInformation(generics.CreateAPIView):
    serializer_class = VehicleInformationSerializer
    queryset = VehicleInformation.objects.all()


class ListVehicleInformation(generics.ListAPIView):
    serializer_class = VehicleInformationSerializer
    queryset = VehicleInformation.objects.all()


class DetailVehicleInformation(generics.RetrieveAPIView):
    serializer_class = VehicleInformationSerializer
    queryset = VehicleInformation.objects.all()


class EditVehicleInformation(generics.UpdateAPIView):
    serializer_class = VehicleInformationSerializer
    queryset = VehicleInformation.objects.all()


class DeleteVehicleInformation(generics.DestroyAPIView):
    serializer_class = VehicleInformationSerializer
    queryset = VehicleInformation.objects.all()


# Service Type Views
class CreateServiceType(generics.CreateAPIView):
    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.all()


class ListServiceType(generics.ListAPIView):
    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.all()


class EditServiceType(generics.UpdateAPIView):
    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.all()


class DeleteServiceType(generics.DestroyAPIView):
    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.all()


class DetailServiceType(generics.RetrieveAPIView):
    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.all()


# Engine Oil Views
class CreateEngineOil(generics.CreateAPIView):
    serializer_class = EngineOilSerializer
    queryset = EngineOil.objects.all()


class ListEngineOil(generics.ListAPIView):
    serializer_class = EngineOilSerializer
    queryset = EngineOil.objects.all()


class DetailEngineOil(generics.RetrieveAPIView):
    serializer_class = EngineOilSerializer
    queryset = EngineOil.objects.all()


class DeleteEgineOil(generics.DestroyAPIView):
    serializer_class = EngineOilSerializer
    queryset = EngineOil.objects.all()


class EditEngioneOil(generics.UpdateAPIView):
    serializer_class = EngineOilSerializer
    queryset = EngineOil.objects.all()


# # Booking Views
# class CreateBooking(generics.CreateAPIView):
#     serializer_class = BookingSerializer
#     queryset = Booking.objects.all()


# class ListBooking(generics.ListAPIView):
#     serializer_class = BookingSerializer
#     queryset = Booking.objects.all()


# class DetailBooking(generics.RetrieveAPIView):
#     serializer_class = BookingSerializer
#     queryset = Booking.objects.all()


# class EditBooking(generics.UpdateAPIView):
#     serializer_class = BookingSerializer
#     queryset = Booking.objects.all()


# class DeleteBooking(generics.DestroyAPIView):
#     serializer_class = BookingSerializer
#     queryset = Booking.objects.all()


# Booking Service Views
# class ListCreateBookingService(generics.ListCreateAPIView):
#     serializer_class = BookingServiceSerializer
#     queryset = BookingService.objects.all()


# class EditDeleteBookingService(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = BookingServiceSerializer
#     queryset = BookingService.objects.all()


# Tyre Views
class CreateTyre(generics.CreateAPIView):
    serializer_class = TyreSerializer
    queryset = Tyre.objects.all()


class ListTyre(generics.ListAPIView):
    serializer_class = TyreSerializer
    queryset = Tyre.objects.all()


class DetailTyre(generics.RetrieveAPIView):
    serializer_class = TyreSerializer
    queryset = Tyre.objects.all()


class DeleteTyre(generics.DestroyAPIView):
    serializer_class = TyreSerializer
    queryset = Tyre.objects.all()


class EditTyre(generics.UpdateAPIView):
    serializer_class = TyreSerializer
    queryset = Tyre.objects.all()


# Views for CarWash
class CreateCarWash(generics.CreateAPIView):
    serializer_class = CarWashSerializer
    queryset = CarWash.objects.all()


class ListCarWash(generics.ListAPIView):
    serializer_class = CarWashSerializer
    queryset = CarWash.objects.all()


class DeleteCarWash(generics.DestroyAPIView):
    serializer_class = CarWashSerializer
    queryset = CarWash.objects.all()


class DetailCarWash(generics.RetrieveAPIView):
    serializer_class = CarWashSerializer
    queryset = CarWash.objects.all()


class EditCarWash(generics.UpdateAPIView):
    serializer_class = CarWashSerializer
    queryset = CarWash.objects.all()


# Views for Fuel
class CreateGasLineDetails(generics.CreateAPIView):
    serializer_class = GasLineDetailsSerializer
    queryset = GasLineDetails.objects.all()


class ListGasLineDetails(generics.ListAPIView):
    serializer_class = GasLineDetailsSerializer
    queryset = GasLineDetails.objects.all()


class EditGasLineDetails(generics.UpdateAPIView):
    serializer_class = GasLineDetailsSerializer
    queryset = GasLineDetails.objects.all()


class deleteGasLineDetails(generics.UpdateAPIView):
    serializer_class = GasLineDetailsSerializer
    queryset = GasLineDetails.objects.all()


class GasLineDetails(generics.RetrieveAPIView):
    serializer_class = GasLineDetailsSerializer
    queryset = GasLineDetails.objects.all()


# Views for Subscriptions
class CreateSubscription(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


class ListSubscriptions(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


class EditSubscription(generics.UpdateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


class DetailSubscription(generics.RetrieveAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


class DeleteSubscription(generics.DestroyAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
