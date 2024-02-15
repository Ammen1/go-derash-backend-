from datetime import datetime
from decimal import Decimal
from math import ceil

from celery import shared_task
from django.db.models import F
from django.db import transaction

from .models import Promotion


@shared_task()
def promotion_prices(reduction_amount, obj_id):
    reduction = Decimal(reduction_amount) / 100
    store_prices = Promotion.products_on_promotion.through.objects.filter(
        promotion_id=obj_id).values_list('product_inventory__store_price', flat=True)

    new_prices = [ceil(price - (price * reduction)) for price in store_prices]

    with transaction.atomic():
        Promotion.products_on_promotion.through.objects.filter(promotion_id=obj_id, price_override=False).update(
            promo_price=F('promo_price') - F('promo_price') * reduction
        )


@shared_task()
def promotion_management():
    now = datetime.now().date()

    with transaction.atomic():
        Promotion.objects.filter(is_schedule=True).update(
            is_active=F('promo_start') <= now and F('promo_end') >= now,
            is_schedule=F('promo_end') >= now
        )
