import graphene

from user_management.models import User

from user_management.schema.types.user import UserConnection

from selony_backend.custom_decorator import permission_required
from selony_backend.custom_permission import is_authenticated, is_superuser


class UserQueries(graphene.ObjectType):

    get_users = graphene.relay.ConnectionField(UserConnection)


    @permission_required(is_superuser)
    @permission_required(is_authenticated)
    def resolve_get_users(root, info, **kwargs):

        return User.objects.all()
