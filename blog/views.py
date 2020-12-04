from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user, allowed_users, admin_only
from .models import *
from .forms import *
from itertools import chain
from django.http import JsonResponse
import json


def home(request):

    if request.user.is_authenticated:
        cliente = Cliente.objects.get(id_user = request.user.id).documento
        order, created = Order.objects.get_or_create(cliente=cliente, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    productos = Producto.objects.all()
    context = {'productos': productos, 'cartItems':cartItems}
    return render(request, "home.html", context)


@allowed_users(allowed_roles=['clientes'])
def cliente(request):
    productos = Producto.objects.all().order_by('id_producto')
    context = {'productos': productos}
    return render(request, "cliente.html", context)


@allowed_users(allowed_roles=['clientes'])
def perfil_cliente(request):
    clientes = Cliente.objects.all()
    try:
        cliente = Cliente.objects.get(id_user_id=request.user.id)
    except:
        cliente = None

    if cliente is None:
        form = InfoCliente()
    else:
        form = InfoCliente(instance=cliente)
    if request.method == 'POST':
        if cliente is None:
            form = InfoCliente(request.POST)
        else:
            form = InfoCliente(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente')
        else:
            print('no es valido')

    context = {'form': form, 'cliente': clientes}
    return render(request, 'perfil_cliente.html', context)


@allowed_users(allowed_roles=['domiciliarios'])
def domiciliario(request):
    return render(request, "domiciliario.html", {})


@allowed_users(allowed_roles=['administrador'])
def administrador(request):
    productos = Producto.objects.all()
    for i in Producto.objects.all():
        try:
            productos.append(Chocolate.objects.all().get(id_producto_id=i.id_producto).tipo)
        except:
            break
    goma = Goma.objects.all()
    flor = Flor.objects.all()
    context = {'productos': productos}
    return render(request, "administrador.html", context)


@allowed_users(allowed_roles=['administrador'])
def crear_producto(request):
    form = CrearProducto(request.POST, request.FILES)
    ultimo = Producto.objects.last().id_producto + 1
    if request.method == 'POST':
        form = CrearProducto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tipo')
        else:
            print('no es valido')
    context = {'form': form, 'ultimo': ultimo}
    return render(request, 'crear_producto.html', context)


@allowed_users(allowed_roles=['administrador'])
def tipo(request):
    return render(request, 'tipo.html', {})


@allowed_users(allowed_roles=['administrador'])
def crear_arreglo_chocolate(request):
    return render(request, 'arreglo_chocolate.html', {})


@allowed_users(allowed_roles=['administrador'])
def crear_arreglo_goma(request):
    return render(request, 'arreglo_goma.html', {})


@allowed_users(allowed_roles=['administrador'])
def crear_caja_chocolate(request):
    return render(request, 'caja_chocolate.html', {})


@allowed_users(allowed_roles=['administrador'])
def crear_caja_goma(request):
    return render(request, 'caja_chocolate.html', {})


@allowed_users(allowed_roles=['administrador'])
def crear_flores(request):
    return render(request, 'flores.html', {})


def cart(request):
    if request.user.is_authenticated:
        cliente = Cliente.objects.get(id_user = request.user.id).documento
        order, created = Order.objects.get_or_create(cliente=cliente, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        cliente = Cliente.objects.get(id_user = request.user.id).documento
        order, created = Order.objects.get_or_create(cliente=cliente, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'checkout.html', context)


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	cliente = Cliente.objects.get(id_user = request.user.id).documento
	product = Producto.objects.get(id_producto=productId)
	order, created = Order.objects.get_or_create(cliente=cliente, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)