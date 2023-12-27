from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/base/", include("core.base.urls", namespace="base")),
    path("api/account/", include("core.account.urls", namespace="account")),
    path('api/basket/', include("core.basket.urls", namespace='basket')),
    path('api/orders/', include('core.orders.urls', namespace='orders')),
    path('api/checkout/', include('core.checkout.urls', namespace='checkout')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
