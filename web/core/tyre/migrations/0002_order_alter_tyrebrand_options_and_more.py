# Generated by Django 4.2.8 on 2024-02-10 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tyre', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('total_paid', models.DecimalField(decimal_places=2, max_digits=5)),
                ('order_key', models.CharField(max_length=200)),
                ('payment_option', models.CharField(blank=True, choices=[('option1', 'Option 1'), ('option2', 'Option 2')], max_length=200)),
                ('billing_status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AlterModelOptions(
            name='tyrebrand',
            options={'ordering': ['name'], 'verbose_name_plural': 'brands'},
        ),
        migrations.AlterModelOptions(
            name='tyrecategory',
            options={'ordering': ['name'], 'verbose_name_plural': 'tyre categories'},
        ),
        migrations.RemoveField(
            model_name='tyre',
            name='arrivaltime',
        ),
        migrations.RemoveField(
            model_name='tyre',
            name='car_type',
        ),
        migrations.RemoveField(
            model_name='tyre',
            name='delivery_address',
        ),
        migrations.RemoveField(
            model_name='tyre',
            name='qty',
        ),
        migrations.RemoveField(
            model_name='tyre',
            name='total_cost',
        ),
        migrations.RemoveField(
            model_name='tyrecategory',
            name='description',
        ),
        migrations.RemoveField(
            model_name='tyrecategory',
            name='image',
        ),
        migrations.RemoveField(
            model_name='tyrecategory',
            name='price',
        ),
        migrations.AddField(
            model_name='tyre',
            name='discount_price',
            field=models.DecimalField(decimal_places=2, default=0, error_messages={'max_digits': {'max_length': 'The price must be between 0 and 999999.99.'}}, help_text='Maximum 999999.99', max_digits=8, verbose_name='Discount price'),
        ),
        migrations.AddField(
            model_name='tyre',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='tyre_images/'),
        ),
        migrations.AddField(
            model_name='tyre',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Change product visibility', verbose_name='Product visibility'),
        ),
        migrations.AddField(
            model_name='tyre',
            name='regular_price',
            field=models.DecimalField(decimal_places=2, default=0, error_messages={'max_digits': {'max_length': 'The price must be between 0 and 999999.99.'}}, help_text='Maximum 999999.99', max_digits=8, verbose_name='Regular price'),
        ),
        migrations.AddField(
            model_name='tyre',
            name='slug',
            field=models.SlugField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='tyre',
            name='title',
            field=models.CharField(default='', help_text='Required', max_length=255, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='tyre',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='tyre',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tyre_brands', to='tyre.tyrebrand'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='tyre.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='tyre.tyre')),
            ],
        ),
    ]
