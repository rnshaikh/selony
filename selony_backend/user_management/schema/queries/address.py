import graphene

from graphene_django.filter import DjangoFilterConnectionField

from user_management.models import Address

from user_management.schema.types.address import AddressType

from selony_backend.custom_decorator import permission_required
from selony_backend.custom_permission import is_authenticated
from selony_backend.custom_filter import AddressFilter


class AddressQueries(graphene.ObjectType):

    addresses = DjangoFilterConnectionField(AddressType,
                                            filterset_class=AddressFilter)

    @permission_required(is_authenticated)
    def resolve_addresses(root, info, **kwargs):

        if info.context.user.is_superuser:
            addresses = Address.objects.all()
        else:
            addresses = Address.objects.filter(created_by=info.context.user)
        return addresses
