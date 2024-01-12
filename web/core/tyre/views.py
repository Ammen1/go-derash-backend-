from django.core.management.base import CommandError
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from core.tyre.models import *
from core.account.models import NewUser
from core.base.models import VehicleInformation
from .serializers import *


# Tyre Views
class CreateTyre(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer = TyreSerializer(data=request.data)
        if serializer.is_valid():
            category_name = serializer.validated_data.get("category")
            category, created = TyreCategory.objects.get_or_create(
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


class ListTyre(generics.ListAPIView):
    serializer_class = TyreSerializer
    queryset = Tyre.objects.all()


class DetailTyre(generics.RetrieveAPIView):
    serializer_class = TyreSerializer
    queryset = Tyre.objects.all()


class DeleteTyre(generics.DestroyAPIView):
    serializer_class = TyreSerializer
    queryset = Tyre.objects.all()


class UpdateTyre(generics.UpdateAPIView):
    serializer_class = TyreSerializer
    queryset = Tyre.objects.all()


# views for TyreCategory
class CreateTyreCategory(generics.CreateAPIView):
    serializer_class = TyreCategorySerializer
    queryset = TyreCategory.objects.all()


class ListTyreCategory(generics.ListAPIView):
    serializer_class = TyreCategorySerializer
    queryset = TyreCategory.objects.all()


class DetailTyreCategory(generics.RetrieveAPIView):
    serializer_class = TyreCategorySerializer
    queryset = TyreCategory.objects.all()


class DeleteTyreCategory(generics.DestroyAPIView):
    serializer_class = TyreCategorySerializer
    queryset = TyreCategory.objects.all()


class UpdateTyreCategory(generics.UpdateAPIView):
    serializer_class = TyreCategorySerializer
    queryset = TyreCategory.objects.all()


# views for TyreBrand
class CreateTyreBrand(generics.CreateAPIView):
    serializer_class = BrandSerializer
    queryset = TyreBrand.objects.all()


class ListTyreBrand(generics.ListAPIView):
    serializer_class = BrandSerializer
    queryset = TyreBrand.objects.all()


class DetailTyreBrand(generics.RetrieveAPIView):
    serializer_class = TyreCategorySerializer
    queryset = TyreBrand.objects.all()


class DeleteTyreBrand(generics.DestroyAPIView):
    serializer_class = BrandSerializer
    queryset = TyreBrand.objects.all()


class UpdateTyreBrand(generics.UpdateAPIView):
    serializer_class = BrandSerializer
    queryset = TyreBrand.objects.all()


# views for order;
# class CreateOrder(generics.CreateAPIView):
#     def post(self, request, *args, **kwargs):
#         serializer = OrderSerializer(data=request.data)

#         if serializer.is_valid():
#             user_id = serializer.validated_data.get("user")
#             user, created = NewUser.objects.get_or_create(
#                 name=user_id)

#             serializer.validated_data["user"] = user
#             serializer.save()
#             return Response(serializer.data, statu=status.HTTP_201_CREATED)
#         print(serializer.errors)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# class ListOrder(generics.ListAPIView):
#     serializer_class = OrderSerializer
#     queryset = Order.objects.all()


# class DetailOrder(generics.RetrieveAPIView):
#     serializer_class = OrderSerializer
#     queryset = Order.objects.all()


# class DeteleOrder(generics.DestroyAPIView):
#     serializer_class = OrderSerializer
#     queryset = Order.objects.all()


# class UpdateOrder(generics.UpdateAPIView):
#     serializer_class = OrderSerializer
#     queryset = Order.objects.all()
