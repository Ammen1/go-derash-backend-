# Generated by Django 4.2.8 on 2024-02-09 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='driver_photo',
            field=models.ImageField(blank=True, default='', null=True, upload_to='driver_photos/'),
        ),
    ]
