from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import ClientUser
from .tables import ClientUserTable
from .forms import ClientUserForm


# Create your views here.

def index(request):
    clients = ClientUser.objects.all()
    sort = request.GET.get('sort', None)
    if sort:
        clients = clients.order_by(sort)
    table = ClientUserTable(clients)
    context = {
        "clients": clients,
        "table": table,
        "add_url": reverse("add-client")
    }
    return render(request, "index.html", context)


def add_client(request):
    if request.method == "POST":
        form = ClientUserForm(request.POST)
        if form.is_valid():
            client = form.save()
            return redirect('index')
    else:
        form = ClientUserForm()
    context = {
        'form': form,
        "back_url": reverse("index")
    }
    return render(request, "add_update.html", context)


def edit_client(request, pk):
    client = get_object_or_404(ClientUser, pk=pk)
    if request.method == "POST":
        form = ClientUserForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save()
            return redirect('index')
    else:
        form = ClientUserForm(instance=client)
    context = {
        'form': form,
        "back_url": reverse("index")
    }
    return render(request, "add_update.html", context)


def delete_client(request, pk):
    client = get_object_or_404(ClientUser, pk=pk)
    client.delete()
    return redirect("index")
