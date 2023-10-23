import graphene

from django.shortcuts import get_object_or_404

from graphql_relay import from_global_id

from user_management.models import Address, User
from user_management.schema.types.address import AddressType

from selony_backend.custom_decorator import permission_required
from selony_backend.custom_permission import is_authenticated


class AddressInputType(graphene.InputObjectType):

    street_address_1 = graphene.String()
    street_address_2 = graphene.String()
    city = graphene.String()
    state = graphene.String()
    country = graphene.String()
    country_code = graphene.String()
    postal_code = graphene.String()
    company = graphene.String()
    created_by = graphene.ID(required=False)
    updated_by = graphene.ID(required=False)


class AddressCreate(graphene.Mutation):

    class Arguments:
        address = graphene.Argument(AddressInputType, required=True)

    address = graphene.Field(AddressType)

    @permission_required(is_authenticated)
    def mutate(parent, info, **kwargs):

        address = kwargs.get('address', None)
        created_by = address.get('created_by', None)

        if info.context.user.is_superuser:
            if not created_by:
                raise Exception("created_by is required")

            created_by = from_global_id(created_by)[1]
            created_by = get_object_or_404(User, id=created_by)
            address['created_by'] = created_by
        else:
            address['created_by'] = info.context.user

        address_obj = Address(**address)
        address_obj.save()
        return AddressCreate(address=address_obj)


class AddressMutation(graphene.ObjectType):

    create_address = AddressCreate.Field()
