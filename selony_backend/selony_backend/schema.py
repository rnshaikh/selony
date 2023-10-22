import graphene

from user_management.schema.queries.user import UserQueries
from user_management.schema.queries.address import AddressQueries
from user_management.schema.mutations.user_auth import UserAuthMutation


class Query(UserQueries, AddressQueries):
    pass


class Mutation(UserAuthMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)


