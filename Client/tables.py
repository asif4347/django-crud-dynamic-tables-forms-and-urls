import django_tables2 as tables
from django.utils.html import format_html

from .models import ClientUser


class ClientUserTable(tables.Table):
    actions = tables.Column(empty_values=())

    class Meta:
        attrs = {"class": "table table-stripped", "data-add-url": "Url here"}
        model = ClientUser

    def render_actions(self, value, record):
        return format_html(
            "<a class='btn btn-primary btn-sm' href='{}'>Update</a> "
            "<a class='btn btn-danger btn-sm' href='{}'>Delete</a>".format(record.edit_url(), record.delete_url())
        )
