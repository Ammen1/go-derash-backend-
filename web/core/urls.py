from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api", include("core.base.urls", namespace="base")),
    path("api", include("core.users.urls", namespace="users")),
]
