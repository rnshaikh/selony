import graphene

from user_management.schema.queries.user import UserQueries
from user_management.schema.queries.address import AddressQueries
from user_management.schema.mutations.user_auth import UserAuthMutation
from user_management.schema.mutations.address import AddressMutation


class Query(UserQueries, AddressQueries):
    pass


class Mutation(UserAuthMutation, AddressMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)


