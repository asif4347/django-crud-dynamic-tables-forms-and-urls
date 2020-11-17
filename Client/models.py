from django.db import models

# Create your models here.
from django.urls import reverse


class ClientUser(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True, max_length=50)
    phone = models.CharField(max_length=20, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    def edit_url(self):
        return reverse("edit-client", kwargs={"pk": self.pk})

    def delete_url(self):
        return reverse("delete-client", kwargs={"pk": self.pk})
