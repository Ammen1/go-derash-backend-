from django.contrib import admin

from .models import DeliveryOptions, PaymentSelections

admin.site.register(DeliveryOptions)
admin.site.register(PaymentSelections)
