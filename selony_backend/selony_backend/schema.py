import graphene

from user_management.schema.queries.user import UserQueries
from user_management.schema.queries.address import AddressQueries
from user_management.schema.mutations.user_auth import UserAuthMutation
from user_management.schema.mutations.address import AddressMutation

from product_management.schema.queries.product import (CategoryQueries,
                                                       ProductClassQueries,
                                                       ProductQueries)
from product_management.schema.mutations.product import ReviewMutation

from card_management.schema.queries.cart import CartQueries
from card_management.schema.mutations.cart import CartMutation

from order_management.schema.queries.order import OrderQueries
from order_management.schema.mutations.order import OrderMutation


class Query(UserQueries, AddressQueries,
            CategoryQueries, ProductClassQueries,
            ProductQueries, CartQueries, OrderQueries):
    pass


class Mutation(UserAuthMutation, AddressMutation, CartMutation,
               OrderMutation, ReviewMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)


