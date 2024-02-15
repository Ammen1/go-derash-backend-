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


class ProductSpecificationSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = ProductSpecification
        fields = ['name']
        read_only = True
        editable = False

    def get_name(self, obj):
        return obj.name


class ProductTypeSerializer(serializers.ModelSerializer):
    size = ProductSpecificationSerializer()

    class Meta:
        model = ProductType
        fields = '__all__'


class ProductSpecificationValueSerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField()

    class Meta:
        model = ProductSpecificationValue
        fields = ['value']
        read_only = True
        editable = False

    def get_value(self, obj):
        return obj.value


class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ["image", "alt_text", "is_feature"]
        read_only = True
        editable = False

    def get_image(self, obj):
        # if obj.image.self.is_feature == True:
        return obj.image.url


class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()
    brand = BrandSerializer()
    product_type = ProductTypeSerializer()
    product_images = ProductImageSerializer(many=True, read_only=True)
    value = ProductSpecificationValueSerializer(
        many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
