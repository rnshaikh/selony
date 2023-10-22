import graphene

from user_management.models import Address

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


class AddressCreate(graphene.Mutation):

    class Arguments:
        address = graphene.Argument(AddressInputType, required=True)

    address = graphene.Field(AddressType)

    @permission_required(is_authenticated)
    def mutate(self, parent, info, **kwargs):

        address = kwargs.get('address', None)
        address['created_by'] = info.context.user

        address_obj = Address(**address)
        address_obj = address_obj.save()

        return AddressCreate(address=address_obj)


class AddressMutation(graphene.ObjectType):

    create_address = AddressCreate.Field()
