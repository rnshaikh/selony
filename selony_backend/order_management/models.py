from enum import Enum

from django.db import models

from user_management.models.address_models import Address
from product_management.models import ProductVariant

from selony_backend.model_mixin import CreateUserInfo


class OrderStatus(Enum):

    Pending = "Pending"
    Shipped = "Shipped"
    Cancelled = "Cancelled"
    Declined = "Declined"
    AwaitingShipment = "Awaiting Shipment"
    AwaitingPickup = "Awaiting Pickup"
    Compeleted = "Compeleted"

    @classmethod
    def as_tuple(cls):
        return ((item.value, item.name) for item in cls)


class Order(CreateUserInfo):

    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_tax = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=100, choices=OrderStatus.as_tuple())
    last_status_change = models.DateTimeField(blank=True, null=True)
    billing_address = models.ForeignKey(Address,
                                        related_name="order_billing_address",
                                        on_delete=models.DO_NOTHING
                                        )
    shipping_address = models.ForeignKey(Address,
                                         related_name="order_shipping_address",
                                         on_delete=models.DO_NOTHING)

    # def __str__(self):
    #     return self.created_by.email + " " + self.status


class OrderUnit(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant,
                                on_delete=models.CASCADE)
    unit_price_gross = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    quantity = models.IntegerField()
