from django.db import models


class AppPermission(models.Model):
    class Meta:
        managed = False  # No database table creation or deletion  \
        # operations will be performed for this model.

        default_permissions = ()  # disable "add", "change", "delete"
        # and "view" default permissions

        # permissions = (
        #     ('customer_rights', 'Global customer rights'),
        #     ('vendor_rights', 'Global vendor rights'),
        #     ('any_rights', 'Global any rights'),
        # )

