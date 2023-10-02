import graphene

from user_management.schema import UserQueries


class Query(UserQueries):
    pass


schema = graphene.Schema(query=Query)


