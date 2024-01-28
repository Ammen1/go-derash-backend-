from django.shortcuts import render
from core.marketplace.drf.serializer import (
    CategorySerializer,
    ProductInventorySerializer,
    ProductSerializer,
)
from core.marketplace.inventory.models import Category, Product, ProductInventory, Media
from rest_framework.response import Response
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


def get_media_for_product_inventory(request, product_inventory_id):
    try:
        media_objects = Media.objects.filter(
            product_inventory_id=product_inventory_id)
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
