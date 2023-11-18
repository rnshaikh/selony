import graphene

from card_management.models import Cart, CartUnit
from card_management.schema.types.cart import CartConnection, CartUnitConnection

from selony_backend.custom_decorator import permission_required
from selony_backend.custom_permission import is_authenticated


class CartQueries(graphene.ObjectType):

    carts = graphene.relay.ConnectionField(CartConnection)
    cart_units = graphene.relay.ConnectionField(CartUnitConnection)

    @permission_required(is_authenticated)
    def resolve_carts(root, info, **kwargs):
        return Cart.objects.filter(created_by=info.context.user)

    @permission_required(is_authenticated)
    def resolve_cart_units(root, info, **kwargs):
        return CartUnit.objects.filter(card__created_by=info.context.user)
