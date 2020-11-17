from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add', add_client, name="add-client"),
    path('<int:pk>/edit/', edit_client, name="edit-client"),
    path('<int:pk>/delete/', delete_client, name="delete-client"),
]
