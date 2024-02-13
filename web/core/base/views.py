from django.core.management.base import CommandError
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from core.base.models import *
from .serializers import *


class Product_all(generics.ListAPIView):
    queryset = Product.objects.filter(
        is_active=True)
    serializer_class = ProductSerializer


class Category_list(APIView):
    def get(self, request, category_slug=None, format=None):
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category__in=Category.objects.get(name=category_slug).get_descendants(include_self=True))
        serializer = ProductSerializer(products, many=True)
        return Response({'category': category.name, 'products': serializer.data}, status=status.HTTP_200_OK)


class Product_detail(generics.RetrieveAPIView):
    def get(self, request, slug=None, format=None):
        queryset = get_object_or_404(Product, slug=slug, is_active=True)
        serializer_class = ProductSerializer
        lookup_field = 'slug'
