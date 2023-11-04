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


class Card(CreateUserInfo):

    total_quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    last_status_change = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(max_length=125, choices=Status.as_tuple())

    def __str__(self):
        return self.created_by.email + self.status


class CardUnit(models.Model):

    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant,
                                on_delete=models.CASCADE)
    quatity = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    data = models.JSONField(blank=True, null=True)

    def __str__(self):
        return "Card No:" + self.card.id






