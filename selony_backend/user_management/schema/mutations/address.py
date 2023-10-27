import graphene

from django.shortcuts import get_object_or_404
from django.utils import timezone

from graphql_relay import from_global_id

from user_management.models import Address, User
from user_management.schema.types.address import AddressType

from selony_backend.custom_decorator import permission_required
from selony_backend.custom_permission import is_authenticated


class AddressInputType(graphene.InputObjectType):

    id = graphene.ID(required=False)
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


class AddressUpdate(graphene.Mutation):

    class Arguments:
        address = graphene.Argument(AddressInputType, required=True)

    address = graphene.Field(AddressType)

    @permission_required(is_authenticated)
    def mutate(parent, info, **kwargs):

        address = kwargs.get('address', None)
        id = address.pop('id', None)
        if not id:
            raise Exception("id is required")

        id = from_global_id(id)[1]
        address_obj = get_object_or_404(Address, id=id)

        if (not info.context.user.is_superuser and
            info.context.user.id != address_obj.created_by.id):
            raise Exception("not authorized")

        address_obj.__dict__.update(address)
        address_obj.updated_by = info.context.user
        address_obj.update_at = timezone.now()
        address_obj.save()
        return AddressUpdate(address=address_obj)


class AddressDelete(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    success = graphene.Boolean()

    @permission_required(is_authenticated)
    def mutate(parent, info, **kwargs):
        id = kwargs.get('id', None)
        if not id:
            raise Exception("id is required")
        id = from_global_id(id)[1]
        address_obj = get_object_or_404(Address, id=id)

        if (not info.context.user.is_superuser and
            info.context.user.id != address_obj.created_by.id):
            raise Exception("not authorized")

        address_obj = get_object_or_404(Address, id=id)
        address_obj.delete()
        return AddressDelete(success=True)


class AddressDetail(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    success = graphene.Boolean()

    def mutate(parent, info, **kwargs):

        id = kwargs.get('id', None)
        id = from_global_id(id)[0]
        address_obj = get_object_or_404(Address, id=id)
        address_obj.delete()
        return AddressDetail(success=True)


class AddressMutation(graphene.ObjectType):

    create_address = AddressCreate.Field()
    update_address = AddressUpdate.Field()
    delete_address = AddressDelete.Field()
