from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user, allowed_users, admin_only


def home(request):
    return render(request, "home.html", {})


@allowed_users(allowed_roles=['clientes'])
def cliente(request):
    return render(request, "cliente.html", {})


@allowed_users(allowed_roles=['domiciliarios'])
def domiciliario(request):
    return render(request, "domiciliario.html", {})


@allowed_users(allowed_roles=['administrador'])
def administrador(request):
    return render(request, "administrador.html", {})
