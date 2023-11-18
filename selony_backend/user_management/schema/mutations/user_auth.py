import json
import graphene

from django.shortcuts import get_object_or_404
from user_management.models import User

from user_management.utils import generate_oauth_token
from user_management.schema.types.user import UserType


class Register(graphene.relay.ClientIDMutation):

    class Input:
        email = graphene.String()
        password = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()

    user = graphene.Field(UserType)

    @classmethod
    def mutate_and_get_payload(cls, parent, info, email, password, first_name,
                               last_name, **kwargs):

        user = User(email=email, first_name=first_name, last_name=last_name)
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

        user = get_object_or_404(User, email=email)

        if not user.check_password(password):
            raise Exception("Invalid email and password")

        login_success_data = generate_oauth_token(info.context, email, password)

        if login_success_data.status_code != 200:
            raise Exception("Invalid email and password")

        responce_dict = json.loads(login_success_data._content)
        return Login(token_details=responce_dict)


class UserAuthMutation(graphene.ObjectType):

    register = Register.Field()
    login = Login.Field()
