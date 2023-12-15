from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/base/", include("core.base.urls", namespace="base")),
    path("api/account/", include("core.account.urls", namespace="account")),
    path('api/basket/', include("core.basket.urls", namespace='basket')),
    path('api/orders/', include('core.orders.urls', namespace='orders')),
    path('api/checkout/', include('core.checkout.urls', namespace='checkout')),

]
