from django.core.management.base import CommandError
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from core.basket.services import *
from core.base.models import *
from .serializers import *


# Category Views
class CreateCategory(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            if "name" not in serializer.validated_data or serializer.validated_data["name"] is None:
                return Response({"error": "Name field is required"}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetail(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class EditCategory(generics.UpdateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class DeleteCategory(generics.RetrieveDestroyAPIView):
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


# Tyre Views
class CreateTyre(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer = TyreSerializer(data=request.data)
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
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


# Battery Views
class CarWashOrderCreateView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer = CarWashOrderSerializer(data=request.data)
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

# Engine Oil Views


class CreateEngineOil(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer = EngineOilSerializer(data=request.data)
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
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    serializer_class = CarWashOrderSerializer
    queryset = CarWashOrder.objects.all()


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


class ListEngineOil(generics.ListAPIView):
    serializer_class = EngineOilSerializer
    queryset = EngineOil.objects.all()


class DetailEngineOil(generics.RetrieveAPIView):
    serializer_class = EngineOilSerializer
    queryset = EngineOil.objects.all()


class DeleteEgineOil(generics.DestroyAPIView):
    serializer_class = EngineOilSerializer
    queryset = EngineOil.objects.all()

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


class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
