import graphene

from user_management.models import Address

from user_management.schema.types.address import AddressConnection

from selony_backend.custom_decorator import permission_required
from selony_backend.custom_permission import is_authenticated, is_superuser


class AddressQueries(graphene.ObjectType):

    addresses = graphene.relay.ConnectionField(AddressConnection)

    @permission_required(is_superuser)
    @permission_required(is_authenticated)
    def resolve_addresses(root, info, **kwargs):

        addresses = Address.objects.all()
        return addresses
