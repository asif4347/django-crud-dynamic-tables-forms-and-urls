from .models import ClientUser
from rest_framework import serializers


class ClientUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientUser
        fields = "__all__"
