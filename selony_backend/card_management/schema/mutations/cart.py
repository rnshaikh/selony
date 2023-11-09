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
        quantity = graphene.Float(required=True)
        price = graphene.Integer(required=True)


    ok = graphene.Boolean()


    @permission_required(is_authenticated)
    @classmethod
    def mutate_and_get_payload(cls, parent, info, **kwargs):

        variant = kwargs.get('variant', None)
        variant_obj = get_object_or_404(ProductVariant, id=variant)

        cart_obj = Cart.objects.filter(created_by=info.context.user,
                                       status=Status.Active.value)

        if not len(cart_obj):
            cart_obj = Cart(created_by=info.context.user,
                            status=Status.Active.value)
            cart_obj.save()
        else:
            cart_obj = cart_obj[0]

        quantity = kwargs.get('quantity', None)
        price = quantity * variant_obj.price

        cart_unit_obj = CartUnit(variant=variant_obj,
                                 cart=cart_obj,
                                 price = price,
                                 quantity = quantity
                                 )
        cart_obj.total_price += price
        cart_obj.total_quantity += quantity
        cart_obj.save()
        cart_unit_obj.save()

        return AddCartUnit(ok=True)



