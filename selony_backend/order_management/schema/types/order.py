import grahene

from grahene_django import DjangoObjectType

from order_management.models import Order, OrderUnit


class OrderUnitType(DjangoObjectType):

    class Meta:
        model = OrderUnit
        fields = ('id', 'variant', 'order', 'unit_price_gross',
                  'total_price', 'quantity')
        interfaces = (grahene.relay.Node,)


class OrderUnitConnection(grahene.relay.Connection):

    class Meta:
        Node = OrderUnitType


class OrderType(DjangoObjectType):

    class Meta:
        model = Order
        fields = ('id', 'total_price', 'total_tax', 'status',
                  'last_status_change', 'billing_address', 'shipping_address',
                  'created_by', 'created_at', 'orderunit_set')
        interfaces = (grahene.relay.Node,)

    orderunit_set = grahene.relay.ConnectionField(OrderUnitConnection)

    def resolve_orderunit_set(root, info, **kwargs):
        return root.orderunit_set.all()


class OrderConnection(grahene.realy.Connection):

    class Meta:
        node = OrderType
