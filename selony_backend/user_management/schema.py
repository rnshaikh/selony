import json
import graphene

from django.shortcuts import get_object_or_404

from graphene_django import DjangoObjectType
from graphql_relay import from_global_id

from .models import User

from user_management.utils import generate_oauth_token


class UserType(DjangoObjectType):

    class Meta:
        model = User
        fields = ('id', 'is_superuser', 'email', 'avatar', 'password')
        interfaces = (graphene.relay.Node, )


class UserConnection(graphene.relay.Connection):

    class Meta:
        node = UserType


class UserQueries(graphene.ObjectType):

    get_users = graphene.relay.ConnectionField(UserConnection)

    def resolve_get_users(root, info, **kwargs):
        return User.objects.all()


class Register(graphene.relay.ClientIDMutation):

    class Input:
        email = graphene.String()
        password = graphene.String()

    user = graphene.Field(UserType)

    @classmethod
    def mutate_and_get_payload(cls, parent, info, email, password, **kwargs):

        user = User(email=email)
        user.set_password(password)
        user.save()
        return Register(user=user)


class TokenType(graphene.Scalar):

    @staticmethod
    def serialize(token_details):
        return token_details


class Login(graphene.Mutation):

    class Arguments:
        email = graphene.String()
        password = graphene.String()

    token_details = graphene.Field(TokenType)

    def mutate(parent, info, email, password):

        import pdb
        pdb.set_trace()
        user = get_object_or_404(User, email=email)

        if not user.check_password(password):
            raise Exception("Invalid email and password")

        login_success_data = generate_oauth_token(info.context, email, password)

        if login_success_data.status_code != 200:
            raise Exception("Invalid email and password")

        responce_dict = json.loads(login_success_data._content)
        return Login(token_details=responce_dict)


class Mutation(graphene.ObjectType):

    register = Register.Field()
    login = Login.Field()
