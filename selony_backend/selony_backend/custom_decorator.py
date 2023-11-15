
def check_permission(permission, context):

    if callable(permission):
        return permission(context.user)
    else:
        return context.user.has_perm(permission)


def permission_required(permission):
    def outer(func):
        def inner(cls, info, *args, **kwargs):
            if check_permission(permission, info.context):
                return func(cls, info, *args, **kwargs)
            raise Exception("Permission Denied")
        return inner
    return outer
