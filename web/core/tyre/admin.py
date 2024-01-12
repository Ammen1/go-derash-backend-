from django.contrib import admin
from core.tyre.models import (
    TyreCategory,
    TyreBrand,
    Tyre,

)

admin.site.register(TyreCategory),
admin.site.register(TyreBrand),
admin.site.register(Tyre),
