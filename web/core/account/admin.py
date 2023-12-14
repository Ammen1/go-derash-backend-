from django.contrib import admin
from .models import (
    NewUser,
    UserProfile,
    ReferralCoupon,
    PushNotification,
    DriverProfile,
)
admin.site.register(ReferralCoupon)
admin.site.register(DriverProfile)
admin.site.register(NewUser)
admin.site.register(UserProfile)
