from django.db import models
from selony_backend.model_mixin import (CreateUserInfo, UpdateUserInfo)


class Address(CreateUserInfo, UpdateUserInfo):

    street_address_1 = models.CharField(max_length=255)
    street_address_2 = models.CharField(max_length=255, blank=True,
                                        null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    country_code = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=10)
    company = models.CharField(max_length=125, blank=True,
                               null=True)

    def __str__(self):
        return self.street_address_1
