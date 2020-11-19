from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import ClientUser
from .serializers import ClientUserSerializer
from .utils import *


@api_view(["GET"])
def list_clients(request):
    clients = ClientUser.objects.all()
    q_name = request.GET.get('full_name')
    if q_name:
        clients = clients.filter(full_name__icontains=q_name)
    serializer = ClientUserSerializer(clients, many=True)
    data = success_response(serializer.data, "List of clients")
    return Response(data)




@api_view(["POST"])
def create_client(request):
    serializer = ClientUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(success_response(serializer.data))
    else:
        return Response(failure_response(serializer.errors))


@api_view(["PUT"])
def update_client(request, pk):
    client = get_object_or_404(ClientUser, pk=pk)
    serializer = ClientUserSerializer(data=request.data, instance=client)
    if serializer.is_valid():
        serializer.save()
        return Response(success_response(serializer.data))
    else:
        return Response(failure_response(serializer.errors))


@api_view(["DELETE"])
def delete_client(request, pk):
    client = get_object_or_404(ClientUser, pk=pk)
    # serializer = ClientUserSerializer(client)
    client.delete()
    return Response(success_response(msg="Client deleted Success!"))
