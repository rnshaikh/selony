import graphene
import stripe

from graphql_relay import from_global_id

from django.shortcuts import get_object_or_404
from django.conf import settings
from django.utils import timezone

from user_management.models.address_models import Address

from card_management.models import Cart, Status

from order_management.schema.types.order import OrderType, OrderInputType
from order_management.models import Order, OrderUnit, OrderStatus

from selony_backend.custom_decorator import permission_required
from selony_backend.custom_permission import is_authenticated


stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateOrder(graphene.relay.ClientIDMutation):

    class Input:

        order = OrderInputType(required=True)

    ok = graphene.Boolean()
    intent = graphene.String()

    @permission_required(is_authenticated)
    def mutate_and_get_payload(parent, info, **kwargs):

        order = kwargs.get('order', None)
        billing_address = order.get('billing_address', None)
        shipping_address = order.get('shipping_address', None)
        cart_id = order.get('cart', None)
        cart_id = from_global_id(cart_id)[1]
        cart_obj = get_object_or_404(Cart, id=cart_id, status=Status.Active.value)
        cart_units = cart_obj.cartunit_set.all()

        billing_address = from_global_id(billing_address)[1]
        shipping_address = from_global_id(shipping_address)[1]

        billing_address = get_object_or_404(Address, id=billing_address)
        shipping_address = get_object_or_404(Address, id=shipping_address)

        order_obj = Order(total_price=cart_obj.total_price,
                          billing_address=billing_address,
                          shipping_address=shipping_address,
                          status=OrderStatus.Pending.value,
                          last_status_change=timezone.now())
        order_obj.save()
        order_units = []

        for i in cart_units:
            order_unit_obj = OrderUnit(order=order_obj,
                                       variant=i.variant,
                                       quantity=i.quantity,
                                       total_price=i.price,
                                       unit_price_gross=i.variant.price)
            order_unit_obj.save()
            order_units.append(order_unit_obj)

        order_obj.orderunit_set.add(*order_units)
        intent = stripe.PaymentIntent.create(
            amount=int(order_obj.total_price * 100),
            currency='inr',
            automatic_payment_methods={
                'enabled': True,
            },
        )

        return CreateOrder(ok=True, intent=intent['client_secret'])


class OrderMutation(graphene.ObjectType):

    create_order = CreateOrder.Field()
