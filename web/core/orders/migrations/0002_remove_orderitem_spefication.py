# Generated by Django 4.2.8 on 2024-02-13 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='spefication',
        ),
    ]
