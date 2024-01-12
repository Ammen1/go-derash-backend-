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
            name='TyreBrand',
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
            name='TyreCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='price')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tyre.tyrecategory')),
            ],
            options={
                'verbose_name_plural': 'tyrescategory',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tyre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tyre_size', models.CharField(max_length=100)),
                ('tyre_type', models.CharField(max_length=100)),
                ('qty', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('delivery_address', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='price')),
                ('arrivaltime', models.DateTimeField(default=django.utils.timezone.now)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tyrebrandes', to='tyre.tyrebrand')),
                ('car_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_type', to='base.vehicleinformation')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tyres', to='tyre.tyrecategory')),
            ],
        ),
    ]
