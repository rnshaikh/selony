import graphene
from graphene_django import DjangoObjectType

from .models import User


class UserType(DjangoObjectType):

    class Meta:
        model = User
        fields = ('id', 'is_superuser', 'email', 'avatar', 'password')


class UserQueries(graphene.ObjectType):

    get_users = graphene.List(UserType)

    def resolve_get_users(root, info, **kwargs):
        return User.objects.all()
