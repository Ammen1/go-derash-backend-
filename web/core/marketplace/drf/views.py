from django.shortcuts import render
from core.marketplace.drf.serializer import (
    CategorySerializer,
    ProductInventorySerializer,
    ProductSerializer,
)
from core.marketplace.inventory.models import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from django.http import JsonResponse


class CategoryList(APIView):
    """
    Return list of all categories
    """

    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class ProductByCategory(APIView):
    """
    Return product by category
    """

    def get(self, request, query=None):
        queryset = Product.objects.filter(category__slug=query)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductInventoryByWebId(APIView):
    """
    Return Sub Product by WebId
    """

    def get(self, request, query=None):
        queryset = ProductInventory.objects.filter(product__web_id=query)
        serializer = ProductInventorySerializer(queryset, many=True)
        return Response(serializer.data)


class ProducInventorById(generics.RetrieveAPIView):

    """
    Return Sub Product by Id
    """

    def get(self, request, query=None):
        queryset = ProductInventory.objects.filter(product__id=query)
        serializer = ProductInventorySerializer(queryset, many=True)
        return Response(serializer.data)


class DeleteProductInventory(generics.DestroyAPIView):
    """
    Delete Product Inventory
    """
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer()


class EditProductInventory(generics.UpdateAPIView):
    """
    Edit Product Inventory
    """
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer()


class DetailProductInventory(generics.RetrieveAPIView):
    """
    Details for each Product Inventory
    """
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer()


# class CreateProductInventory():
#     """
#     Creaate Product Inventory
#     """

#     queryset = ProductInventory.objects.all()
#     serializer_class = ProductInventorySerializer()


class CreateProductInventory(generics.CreateAPIView):
    serializer_class = ProductInventorySerializer()

    def post(self, request, *args, **kwargs):
        serializer = ProductInventorySerializer(data=request.data)
        if serializer.is_valid():
            product_type = serializer.validated_data.get("product_type")
            product_type, created = ProductType.objects.get_get_or_create(
                name=product_type)
            product = serializer.validated_data.get("product")
            product, created = Product.objects.get_or_create(
                name=product)
            brand = serializers.validate_data.get("brand")
            brand, created = Brand.objects.get_or_create(naem=brand)

            serializer.validated_data["product_type"] = product_type
            serializer.validates_data["product"] = product
            sesrializer.validates_data["brand"] = brand

            serializer.save()
            return Response(serializer.data, statu=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


def get_media_for_product_inventory(request, product_inventory_id):
    try:
        media_objects = Media.objects.filter(
            product_inventory_id=product_inventory_id, is_feature=True)
        media_data = [
            {
                'img_url': media.img_url.url,
                'alt_text': media.alt_text,
                'is_feature': media.is_feature,
                'created_at': media.created_at,
                'updated_at': media.updated_at,
            }
            for media in media_objects
        ]
        return JsonResponse({'media': media_data})
    except Media.DoesNotExist:
        return JsonResponse({'error': 'Media not found for the given product inventory'}, status=404)
