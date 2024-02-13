from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(
        verbose_name=_("Category Name"),
        help_text=_("Required and unique"),
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(verbose_name=_(
        "Category safe URL"), max_length=255, unique=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE,
                            null=True, blank=True, related_name="children")
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def get_absolute_url(self):
        return reverse("base:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(
        verbose_name=_("Product Name"),
        help_text=_("Required"),
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Product Type")
        verbose_name_plural = _("Product Types")

    def __str__(self):
        return self.name


class ProductSpecification(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    name = models.CharField(
        verbose_name=_("Name"),
        help_text=_("Required"),
        max_length=255,
    )

    class Meta:
        verbose_name = _("Product Specification")
        verbose_name_plural = _("Product Specifications")

    def __str__(self):
        return self.name


class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    brand = models.ForeignKey(
        Brand, related_name="products", on_delete=models.RESTRICT)
    title = models.CharField(
        verbose_name=_("Title"),
        help_text=_("Required"),
        max_length=255,
        default="products",
    )
    description = models.TextField(verbose_name=_(
        "Description"), help_text=_("Not Required"), blank=True)
    slug = models.SlugField(max_length=255)
    regular_price = models.DecimalField(
        verbose_name=_("Regular price"),
        max_digits=10,
        decimal_places=2,
    )
    discount_price = models.DecimalField(
        verbose_name=_("Discount price"),
        max_digits=10,
        decimal_places=2,
    )
    is_active = models.BooleanField(
        verbose_name=_("Product visibility"),
        help_text=_("Change product visibility"),
        default=True,
    )
    created_at = models.DateTimeField(
        _("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def get_absolute_url(self):
        return reverse("base:product_detail", args=[self.slug])

    def __str__(self):
        return self.title


class ProductSpecificationValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.ForeignKey(
        ProductSpecification, on_delete=models.RESTRICT)
    value = models.CharField(
        verbose_name=_("Value"),
        help_text=_("Product specification value (maximum of 255 words)"),
        max_length=255,
    )

    class Meta:
        verbose_name = _("Product Specification Value")
        verbose_name_plural = _("Product Specification Values")

    def __str__(self):
        return self.value


def default_image_path():
    return "images/default.png"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(
        verbose_name=_("Image"),
        help_text=_("Upload a product image"),
        upload_to="images/",
        default=default_image_path,
    )
    alt_text = models.CharField(
        verbose_name=_("Alternative text"),
        help_text=_("Please add alternative text"),
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")

    def __str__(self):
        return f"{self.product.title} - Image {self.id}"
