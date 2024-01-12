# Generated by Django 4.2.8 on 2024-01-12 20:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BatteryBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'brandes',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='BatteryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='price')),
                ('is_active', models.BooleanField(default=False)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='battery.batterycategory')),
            ],
            options={
                'verbose_name_plural': 'batterycategories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Battery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_battery_service', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='price')),
                ('qty', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('arrivaltime', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('description', models.TextField()),
                ('delivery_address', models.CharField(max_length=255)),
                ('batteryBrand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batterybrand', to='battery.batterybrand')),
                ('car_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.vehicleinformation')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='batteries', to='battery.batterycategory')),
            ],
        ),
    ]