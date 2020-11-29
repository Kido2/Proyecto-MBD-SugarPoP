from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    return render(request, "home.html", {})


def cliente(request):
    return render(request, "cliente.html", {})
