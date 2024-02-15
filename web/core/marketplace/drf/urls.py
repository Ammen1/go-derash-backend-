from django.urls import path, include

# from core.marketplace.drf.views import (
#     CategoryList,
#     ProductByCategory,
#     ProductInventoryByWebId,
#     ProducInventorById,
#     get_media_for_product_inventory,
# )
from .views import *


app_name = 'drf'

urlpatterns = [
    path("inventory/category/all/", CategoryList.as_view()),
    path("inventory/productinventory/<int:query>/", ProducInventorById.as_view()),
    path(
        "inventory/products/category/<str:query>/",
        ProductByCategory.as_view(),
    ),
    path("inventory/<int:query>/", ProductInventoryByWebId.as_view()),
    # path("api/search/<str:query>/", SearchProductInventory.as_view()),
    path("inventory/media/<int:product_inventory_id>/",
         get_media_for_product_inventory),
    path("inventory/delete/<int:pk>/", DeleteProductInventory.as_view()),
    path("inventory/edit/<int:pk>/", EditProductInventory.as_view()),

]
