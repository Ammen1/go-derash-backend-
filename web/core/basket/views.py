from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from core.base.models import ServiceType
from .serializers import (
    BaseServiceSerializer, BatteryServiceSerializer, EngineOilServiceSerializer,
    TyreServiceSerializer, CarWashServiceSerializer, GasLineServiceSerializer
)


# class BaseServiceView(APIView):
#     def get_serializer_class(self):
#         return BaseServiceSerializer

#     def get_service_type(self, service_type_id):
#         return ServiceType.objects.get(id=service_type_id)

#     def get(self, request, service_type_id):
#         service_type = self.get_service_type(service_type_id)
#         serializer = self.get_serializer_class()(service_type)
#         return Response(serializer.data)


class BaseServiceView(generics.RetrieveAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = BaseServiceSerializer
    lookup_field = 'pk'


class BatteryServiceView(BaseServiceView):
    serializer_class = BatteryServiceSerializer


class EngineOilServiceView(BaseServiceView):
    serializer_class = EngineOilServiceSerializer


class TyreServiceView(BaseServiceView):
    serializer_class = TyreServiceSerializer


class CarWashServiceView(BaseServiceView):
    serializer_class = CarWashServiceSerializer


class GasLineServiceView(BaseServiceView):
    serializer_class = GasLineServiceSerializer
