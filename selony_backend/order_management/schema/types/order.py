import graphene

from graphene_django import DjangoObjectType

from order_management.models import Order, OrderUnit


class OrderUnitType(DjangoObjectType):

    class Meta:
        model = OrderUnit
        fields = ('id', 'variant', 'order', 'unit_price_gross',
                  'total_price', 'quantity')
        interfaces = (graphene.relay.Node,)


class OrderUnitConnection(graphene.relay.Connection):

    class Meta:
        node = OrderUnitType


class OrderType(DjangoObjectType):

    class Meta:
        model = Order
        fields = ('id', 'total_price', 'total_tax', 'status',
                  'last_status_change', 'billing_address', 'shipping_address',
                  'created_by', 'created_at', 'orderunit_set')
        interfaces = (graphene.relay.Node,)

    orderunit_set = graphene.relay.ConnectionField(OrderUnitConnection)

    def resolve_orderunit_set(root, info, **kwargs):
        return root.orderunit_set.all()


class OrderConnection(graphene.relay.Connection):

    class Meta:
        node = OrderType


class OrderInputType(graphene.InputObjectType):

    cart = graphene.ID()
    billing_address = graphene.ID()
    shipping_address = graphene.ID()

