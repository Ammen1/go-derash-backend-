from decimal import Decimal
from django.conf import settings
from core.tyre.models import Tyre
from core.checkout.models import DeliveryOptions


class Basket:
    """
    A generic Basket class for handling multiple types of products or services.
    """

    def __init__(self, request):
        self.session = request.session
        print(self.session)
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if settings.BASKET_SESSION_ID not in request.session:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

        print("total basket ", self.basket)

    def add(self, item, qty, price):
        """
        Adding and updating the basket session data
        """
        item_id = str(item.id)
        print("item_id", item_id)

        if item_id in self.basket:
            self.basket[item_id]["qty"] += qty
        else:
            self.basket[item_id] = {"price": str(price), "qty": qty}

        self.save()

    def __iter__(self):
        """
        Collect the item_id in the session data to query the database
        and return items
        """
        item_ids = self.basket.keys()
        items = Tyre.objects.filter(id__in=item_ids)
        basket = self.basket.copy()

        for item in items:
            basket[str(item.id)]["item"] = item

        for item_data in basket.values():
            item_data["price"] = Decimal(item_data["price"])
            item_data["total_price"] = item_data["price"] * item_data["qty"]
            yield item_data

    def __len__(self):
        """
        Get the basket data and count the qty of items
        """

        return sum(item_data["qty"] for item_data in self.basket.values())

    def update(self, product, qty):
        """
        Update values in session data
        """
        product_id = str(product)
        if product_id in self.basket:
            self.basket[product_id]["qty"] = qty
        self.save()

    def get_subtotal_price(self):
        return sum(Decimal(item_data["price"]) * item_data["qty"] for item_data in self.basket.values())

    def get_delivery_price(self):
        new_price = 0.00

        if "purchase" in self.session:
            new_price = DeliveryOptions.objects.get(
                id=self.session["purchase"]["delivery_id"]).delivery_price

        return new_price

    def get_total_price(self):
        new_price = 0.00
        subtotal = sum(Decimal(item_data["price"]) * item_data["qty"]
                       for item_data in self.basket.values())

        if "purchase" in self.session:
            new_price = DeliveryOptions.objects.get(
                id=self.session["purchase"]["delivery_id"]).delivery_price

        total = subtotal + Decimal(new_price)
        print("totalabush", total)
        return total

    def basket_update_delivery(self, delivery_price=0):
        subtotal = sum(Decimal(item_data["price"]) * item_data["qty"]
                       for item_data in self.basket.values())
        total = subtotal + Decimal(delivery_price)
        print("totalamen", total)
        return total

    def delete(self, item):
        """
        Delete item from session data
        """
        item_id = str(item.id)

        if item_id in self.basket:
            del self.basket[item_id]
            self.save()

    def clear(self):
        # Remove basket from session
        self.session.pop(settings.BASKET_SESSION_ID, None)
        self.session.pop("address", None)
        self.session.pop("purchase", None)
        self.save()

    def save(self):
        self.session.modified = True
