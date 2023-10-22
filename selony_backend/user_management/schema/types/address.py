import graphene

from graphene_django import DjangoObjectType

from graphql_relay import from_global_id

from user_management.models import Address


class AddressType(DjangoObjectType):

    class Meta:

        model = Address
        fields = ('street_address_1', 'street_address_2', 'city',
                  'state', 'country', 'country_code', 'postal_code',
                  'company', 'created_by', 'created_at', 'updated_by',
                  'updated_at')
        interfaces = (graphene.relay.Node,)


class AddressConnection(graphene.relay.Connection):

    class Meta:
        node = AddressType



