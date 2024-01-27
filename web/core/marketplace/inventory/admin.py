from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from django.core.validators import MinValueValidator
from decimal import Decimal

from .models import (
    Category,
    Product,
    Brand,
    ProductAttribute,
    ProductType,
    ProductAttributeValue,
    ProductInventory,
    Media,
    Stock,
    ProductAttributeValues,
    ProductTypeAttribute,
)


class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue


class ProductInventoryInline(admin.TabularInline):
    model = ProductInventory
    extra = 1


class ProductTypeAttributeInline(admin.TabularInline):
    model = ProductTypeAttribute


class MediaInline(admin.TabularInline):
    model = Media


class StockInline(admin.TabularInline):
    model = Stock


class ProductAttributeValuesInline(admin.TabularInline):
    model = ProductAttributeValues


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ['name', 'slug', 'is_active']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'category',
                    'is_active', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [ProductTypeAttributeInline]
    list_display = ['name']


@admin.register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    list_display = ['product_attribute', 'attribute_value']


@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    inlines = [ProductAttributeValuesInline, MediaInline]
    list_display = ['sku', 'upc', 'product_type', 'product', 'brand', 'is_active', 'is_default', 'retail_price',
                    'store_price', 'is_digital', 'weight', 'created_at', 'updated_at']


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['product_inventory', 'img_url',
                    'alt_text', 'is_feature', 'created_at', 'updated_at']


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['product_inventory', 'last_checked', 'units', 'units_sold']


@admin.register(ProductAttributeValues)
class ProductAttributeValuesAdmin(admin.ModelAdmin):
    list_display = ['attributevalues', 'productinventory']


@admin.register(ProductTypeAttribute)
class ProductTypeAttributeAdmin(admin.ModelAdmin):
    list_display = ['product_attribute', 'product_type']
