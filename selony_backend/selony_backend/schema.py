import graphene

from user_management.schema import UserQueries, Mutation


class Query(UserQueries):
    pass


class Mutation(Mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)


