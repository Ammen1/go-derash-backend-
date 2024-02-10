from django.contrib import admin
from core.tyre.models import (
    TyreCategory,
    TyreBrand,
    Tyre,
    Order,
    OrderItem

)

admin.site.register(TyreCategory),
admin.site.register(TyreBrand),
admin.site.register(Tyre),
admin.site.register(Order),
admin.site.register(OrderItem),
