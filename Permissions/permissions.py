from Permissions.models import AppPermission

permission_list = [
    ("list_clients", "List all Clients"),
    ("add_client", "Add New Client"),
    ("edit_client", "Edit Client"),
    ("delete_client", "Delete Client"),
]

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# import User model
from django.contrib.auth.models import User


def assign_permission(group_name, ct, permission):
    # print(group_name, permission)
    # return {}
    try:
        new_group, created = Group.objects.get_or_create(name=group_name)

        """
        override auth contenttype for all permissions 
        """
        ct = ContentType.objects.get_for_model(AppPermission)
        permission, created = Permission.objects.get_or_create(codename=permission.get("codename"),
                                                               name=permission.get("name"),
                                                               content_type=ct)
        new_group.permissions.add(permission)
    except:
        pass


def get_permission_details(ct, codename, permission_set: list) -> dict:
    perm = {}
    perms = [perm for perm in permission_set if ct == perm.get("ct")]
    if perms:
        perms = perms[0]
        perm = [perm for perm in perms.get("permissions") if perm.get("codename") == codename]
        if perm.__len__() > 0:
            return perm[0]
    return {}


def create_permissions_from_request(permission_set: list, request):
    for pm in permission_set:
        ct = pm.get("ct")
        form_perm_list = request.POST.getlist(ct)
        if form_perm_list:
            for codename in form_perm_list:
                permission_obj = get_permission_details(ct, codename, permission_set)
                assign_permission(request.POST["group_name"], ct, permission_obj)


permission_sets = [
    {
        "title": "Dashboard",
        "ct": "dashboard",
        "permissions": [
            {
                "codename": "view_dashboard",
                "name": "View Dashboard"
            }, {
                "codename": "check_dashboard",
                "name": "Check Dashboard"
            },
        ]
    },
    {
        "title": "Reservations",
        "ct": "reservation",
        "permissions": [
            {
                "codename": "add_reservation",
                "name": "Add Reservation"
            },
            {
                "codename": "edit_reservation",
                "name": "Edit Reservation"
            }, {
                "codename": "delete_reservation",
                "name": "Delete Reservation"
            },
            {
                "codename": "list_reservations",
                "name": "List Reservations"
            }, {
                "codename": "dispatch_reservations",
                "name": "Dispatch Reservations"
            },
        ]
    },
    {
        "title": "Clients",
        "ct": "client",
        "permissions": [
            {
                "codename": "add_client",
                "name": "Add Client"
            },
            {
                "codename": "edit_client",
                "name": "Edit Client"
            }, {
                "codename": "delete_client",
                "name": "Delete Client"
            },
            {
                "codename": "list_clients",
                "name": "List Clients"
            },
        ]
    }
]
