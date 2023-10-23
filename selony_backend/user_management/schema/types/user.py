import graphene

from graphene_django import DjangoObjectType

from user_management.models import User


class UserType(DjangoObjectType):

    full_name = graphene.String()

    class Meta:
        model = User
        fields = ('id', 'is_superuser', 'email', 'avatar',
                  'password', 'first_name', 'last_name', 'full_name')
        interfaces = (graphene.relay.Node, )


class UserConnection(graphene.relay.Connection):

    class Meta:
        node = UserType

