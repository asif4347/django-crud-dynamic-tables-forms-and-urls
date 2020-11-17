from django import forms
from .models import ClientUser


class ClientUserForm(forms.ModelForm):
    class Meta:
        model = ClientUser
        fields = "__all__"

