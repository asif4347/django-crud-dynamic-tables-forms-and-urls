from django.contrib.auth.models import User
from django.utils import six
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test


def group_required(group, login_url=None, raise_exception=False):
    """
    Decorator for views that checks whether a user has a group permission,
    redirecting to the log-in page if necessary.
    If the raise_exception parameter is given the PermissionDenied exception
    is raised.
    """

    def check_perms(user):
        if isinstance(group, six.string_types):
            groups = (group,)
        else:
            groups = group
        # First check if the user has the permission (even anon users)
        if user.groups.filter(name__in=groups).exists():
            return True
        # In case the 403 handler should be called raise the exception
        if raise_exception:
            raise PermissionDenied
        # As the last resort, show the login form
        return False

    return user_passes_test(check_perms, login_url=login_url)


def permission_required(permission, permission_prefix="permission", login_url=None, raise_exception=False):
    """
        Decorator for views that checks whether a user has a permission,
        redirecting to the log-in page if necessary.
        If the raise_exception parameter is given the PermissionDenied exception
        is raised.
    """
    permission = "{}.{}".format(permission_prefix, permission) if permission_prefix else permission

    def check_perms(user: User):
        return user_has_permission(user, permission, raise_exception)

    return user_passes_test(check_perms, login_url=login_url)


def user_has_permission(user: User, permission, raise_exception=False):
    """
     Check if user has permission assigned in group
    """
    if permission in user.get_group_permissions():
        return True
    # In case the 403 handler should be called raise the exception
    if raise_exception:
        raise PermissionDenied
    # As the last resort, show the login form
    return False
