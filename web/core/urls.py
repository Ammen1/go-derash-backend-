from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from core.base.views import index


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/base/", include("core.base.urls", namespace="base")),
    path("api/account/", include("core.account.urls", namespace="account")),
    path('api/basket/', include("core.basket.urls", namespace='basket')),
    path('api/orders/', include('core.orders.urls', namespace='orders')),
    path('api/checkout/', include('core.checkout.urls', namespace='checkout')),
    path('api/fuel/', include('core.fuel.urls', namespace='fuel')),
    path('api/battery/', include('core.battery.urls', namespace='battery')),
    path('api/tyre/', include('core.tyre.urls', namespace='tyre')),
    path('api/engineoil/', include('core.engineoil.urls', namespace='engineoil')),
    path('api/carwash/', include('core.carwash.urls', namespace='carwash')),
    path('api/market/', include('core.market.urls', namespace='market')),
    re_path(r'^.*$', index),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
