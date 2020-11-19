from django.urls import path
from .views_api import *

urlpatterns = [
    path("clients", list_clients, name="api-clients-list"),
    path("clients/add", create_client, name="api-clients-add"),
    path("clients/<int:pk>/update", update_client, name="api-clients-update"),
    path("clients/<int:pk>/delete", delete_client, name="api-clients-delete"),
]
