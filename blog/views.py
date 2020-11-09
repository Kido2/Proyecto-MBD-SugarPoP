from django.shortcuts import render, redirect
from .models import Admin, Client, Domc
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login


def home(request):
	return render(request, "home.html", {})