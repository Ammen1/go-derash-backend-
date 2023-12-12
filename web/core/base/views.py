from django.shortcuts import get_object_or_404
from core.base.models import *
from .serializers import *
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


class CreateService(APIView):
    # parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceList(generics.ListAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class ServiceDaitle(generics.RetrieveAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class EditService(generics.UpdateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class DeleteService(generics.RetrieveDestroyAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


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


class DeleteVehucleInformation(generics.DestroyAPIView):
    serializer_class = VehicleInformationSerializer
    queryset = VehicleInformation.objects.all()


class CreateServiceType(generics.CreateAPIView):
    serializer_class = ServiceTypeSerializer
    queryset = Service.objects.all()


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


class CreateBooking(generics.CreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class ListBooking(generics.ListAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class DetailBooking(generics.RetrieveAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class EditBooking(generics.UpdateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class DeleteBooking(generics.DestroyAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
