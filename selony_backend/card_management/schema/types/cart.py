import graphene

from graphene_django import DjangoObjectType

from card_management.models import Cart, CartUnit


class CartUnitType(DjangoObjectType):

    class Meta:
        model = CartUnit
        fields = ('id', 'cart', 'variant', 'quantity',
                  'price', 'data')
        interfaces = (graphene.relay.Node, )


class CartUnitConnection(graphene.relay.Connection):

    class Meta:
        node = CartUnitType


class CartType(DjangoObjectType):

    class Meta:
        model = Cart
        fields = ('id', 'total_quantity', 'total_price',
                  'last_status_change', 'updated_at', 'created_at',
                  'created_by', 'status', 'cartunit_set')
        interfaces = (graphene.relay.Node, )

    cartunit_set = graphene.relay.ConnectionField(CartUnitConnection)

    def resolve_cartunit_set(root, info, **kwargs):
        return root.cartunit_set.all()


class CartConnection(graphene.relay.Connection):

    class Meta:
        node = CartType
