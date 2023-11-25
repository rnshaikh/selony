import graphene

from graphene_django import DjangoObjectType

from django.shortcuts import get_object_or_404

from order_management.models import Order, OrderUnit
from order_management.schema.types.order import (OrderType,
                                                 OrderConnection,
                                                 OrderUnitConnection)

from selony_backend.custom_decorator import permission_required
from selony_backend.custom_permission import is_authenticated


class OrderQueries(graphene.ObjectType):

    order = graphene.relay.Node.Field(OrderType)
    orders = graphene.relay.ConnectionField(OrderConnection)


    @permission_required(is_authenticated)
    def resolve_producr(root, info, id):
        obj = get_object_or_404(Order, id=id)
        return obj

    @permission_required(is_authenticated)
    def resolve_orders(root, info, **kwargs):
        return Order.objects.prefetch_related('orderunit_set').filter(created_by=info.context.user)

