from enum import Enum

from django.db import models

from product_management.models import ProductVariant

from selony_backend.model_mixin import CreateUserInfo


class Status(Enum):

    Active = "Active"
    Discarded = "Discarded"
    Completed = "Completed"

    @classmethod
    def as_tuple(cls):
        return ((item.value, item.name) for item in cls)


class Cart(CreateUserInfo):

    total_quantity = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    last_status_change = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(max_length=125, choices=Status.as_tuple())

    def __str__(self):
        return self.created_by.email + " " + self.status


class CartUnit(models.Model):

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    data = models.JSONField(blank=True, null=True)

    def __str__(self):
        return "Cart No: " + str(self.cart.id)






