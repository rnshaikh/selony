import graphene

from django.utils import timezone
from django.shortcuts import get_object_or_404

from graphql_relay import from_global_id

from card_management.models import Cart, CartUnit, Status

from product_management.models import ProductVariant

from selony_backend.custom_decorator import permission_required
from selony_backend.custom_permission import is_authenticated


class AddCartUnit(graphene.relay.ClientIDMutation):

    class Input:

        variant = graphene.ID(required=True)
        quantity = graphene.Int(required=True)

    ok = graphene.Boolean()

    @permission_required(is_authenticated)
    def mutate_and_get_payload(parent, info, **kwargs):

        variant = kwargs.get('variant', None)
        variant = from_global_id(variant)[1]
        variant_obj = get_object_or_404(ProductVariant, id=variant)

        cart_obj = Cart.objects.filter(created_by=info.context.user,
                                       status=Status.Active.value)

        if not len(cart_obj):
            cart_obj = Cart(created_by=info.context.user,
                            status=Status.Active.value)
            cart_obj.total_quantity = 0
            cart_obj.save()
        else:
            cart_obj = cart_obj[0]

            if cart_obj.created_by != info.context.user:
                raise Exception("Permission Denied")

        quantity = kwargs.get('quantity', 0)
        price = quantity * variant_obj.price

        try:
            cart_unit_obj = CartUnit.objects.get(cart=cart_obj, variant=variant_obj)

        except CartUnit.DoesNotExist:
            cart_unit_obj = CartUnit(variant=variant_obj,
                                     cart=cart_obj,
                                     price=0,
                                     quantity=0)

        cart_unit_obj.price += price
        cart_unit_obj.quantity += quantity
        cart_unit_obj.save()

        cart_obj.total_price += price
        cart_obj.total_quantity += quantity
        cart_obj.save()
        cart_unit_obj.save()

        return AddCartUnit(ok=True)


class RemoveCartUnit(graphene.relay.ClientIDMutation):

    class Input:
        card_unit_id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @permission_required(is_authenticated)
    def mutate_and_get_payload(parent, info, **kwargs):

        card_unit_id = kwargs.get('card_unit_id', None)
        id = from_global_id(card_unit_id)[1]
        obj = get_object_or_404(CartUnit, id=id)

        if obj.cart.created_by != info.context.user:
            raise Exception("Permission Denied")

        obj.cart.total_quantity = obj.cart.total_quantity - obj.quantity
        obj.cart.total_price = obj.cart.total_price - obj.price
        obj.cart.save()
        obj.delete()
        return RemoveCartUnit(ok=True)


class RemoveCart(graphene.relay.ClientIDMutation):

    class Input:
        cart_id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @permission_required(is_authenticated)
    def mutate_and_get_payload(parent, info, **kwargs):

        cart_id = kwargs.get('cart_id', None)
        id = from_global_id(cart_id)[1]

        obj = get_object_or_404(Cart, id=id)

        if obj.created_by != info.context.user:
            raise Exception("Permission Denied")

        obj.status = Status.Discarded.value
        obj.save()
        return RemoveCart(ok=True)


class CartMutation(graphene.ObjectType):

    add_cart_unit = AddCartUnit.Field()
    remove_cart_unit = RemoveCartUnit.Field()
    remove_cart = RemoveCart.Field()