# Generated by Django 4.2.8 on 2024-02-13 17:35

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('coupon_code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProductsOnPromotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promo_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('price_override', models.BooleanField(default=False)),
                ('product_inventory_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ProductInventoryOnPromotion', to='inventory.productinventory')),
            ],
        ),
        migrations.CreateModel(
            name='PromoType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('promo_reduction', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=False)),
                ('is_schedule', models.BooleanField(default=False)),
                ('promo_start', models.DateField()),
                ('promo_end', models.DateField()),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='coupon', to='promotion.coupon')),
                ('products_on_promotion', models.ManyToManyField(related_name='products_on_promotion', through='promotion.ProductsOnPromotion', to='inventory.productinventory')),
                ('promo_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='promotype', to='promotion.promotype')),
            ],
        ),
        migrations.AddField(
            model_name='productsonpromotion',
            name='promotion_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promotion', to='promotion.promotion'),
        ),
        migrations.AlterUniqueTogether(
            name='productsonpromotion',
            unique_together={('product_inventory_id', 'promotion_id')},
        ),
    ]
