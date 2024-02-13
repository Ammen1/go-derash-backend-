from rest_framework import serializers
from django.conf import settings
from attr import attributes
from django.core.exceptions import ObjectDoesNotExist
from core.base.models import *
from rest_framework import serializers
from core.account.serializers import CustomUserSerializer


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSpecificationValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecificationValue
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductType
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()
    brand = BrandSerializer()
    product_type = ProductTypeSerializer()
    # product_images = ProductImageSerializer()

    class Meta:
        model = Product
        fields = '__all__'
