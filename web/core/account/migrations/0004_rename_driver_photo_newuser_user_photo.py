# Generated by Django 4.2.8 on 2024-02-09 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_adminuser_user_car'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newuser',
            old_name='driver_photo',
            new_name='user_photo',
        ),
    ]
