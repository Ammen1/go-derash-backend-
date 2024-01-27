from django.urls import path, include

from core.marketplace.drf.views import (
    CategoryList,
    ProductByCategory,
    ProductInventoryByWebId,
)
# from ecommerce.search.views import SearchProductInventory


app_name = 'drf'

urlpatterns = [
    path("inventory/category/all/", CategoryList.as_view()),
    path(
        "inventory/products/category/<str:query>/",
        ProductByCategory.as_view(),
    ),
    path("inventory/<int:query>/", ProductInventoryByWebId.as_view()),
    # path("api/search/<str:query>/", SearchProductInventory.as_view()),
]
