from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from accounts.decorators import unauthenticated_user
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only
# Create your views here.


def role(request):
    return render(request, 'accounts/role.html')


@unauthenticated_user
def registrar_cliente(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='clientes')
            user.groups.add(group)

            messages.success(request, 'La cuenta fue creada para ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/registrar_cliente.html', context)


@unauthenticated_user
def registrar_domiciliario(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='domiciliarios')
            user.groups.add(group)

            messages.success(request, 'La cuenta fue creada para ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/registrar_domiciliario.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        cliente = Group.objects.get(name="clientes").user_set.all()
        domiciliario = Group.objects.get(name="domiciliarios").user_set.all()
        if user is not None:
            if user in cliente:
                login(request, user)
                return redirect('cliente')
            elif user in domiciliario:
                login(request, user)
                return redirect('domiciliario')
            else:
                login(request, user)
                return redirect('administrador')
        else:
            messages.info(request, 'Usuario o contraseña incorrectos')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')
