from django.contrib import admin

from order_management.models import Order, OrderUnit

admin.site.register(Order)
admin.site.register(OrderUnit)
