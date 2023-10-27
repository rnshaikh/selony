
def is_authenticated(user):
    return bool(user and user.is_authenticated)


def is_superuser(user):
    return bool(user and user.is_superuser)
