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


@allowed_users(allowed_roles=['domiciliarios'])
def perfil_domiciliario(request):
    try:
        domiciliario = Domiciliario.objects.get(id_user_id=request.user.id)
    except:
        domiciliario = None

    if domiciliario is None:
        form = CrearDomiciliario()
    else:
        form = CrearDomiciliario(instance=domiciliario)
    if request.method == 'POST':
        if domiciliario is None:
            form = CrearDomiciliario(request.POST)
        else:
            form = CrearDomiciliario(request.POST, instance=domiciliario)
        if form.is_valid():
            form.save()
            return redirect('domiciliario')
        else:
            print('no es valido')

    context = {'form': form}
    return render(request, 'perfil_domiciliario.html', context)


@allowed_users(allowed_roles=['administrador'])
def consultar_domiciliario(request):
    domiciliario = Domiciliario.objects.all()
    context = {'domiciliario': domiciliario}
    return render(request, 'consultar_domiciliario.html', context)



@allowed_users(allowed_roles=['administrador'])
def administrador(request):
    productos = Producto.objects.all().order_by('id_producto')
    context = {'productos': productos}
    return render(request, "administrador.html", context)


@allowed_users(allowed_roles=['administrador'])
def tipo(request):
    return render(request, 'tipo.html', {})


@allowed_users(allowed_roles=['administrador'])
def crear_arreglo_chocolate(request):
    form1 = CrearProducto()
    if request.method == 'POST':
        form1 = CrearProducto(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('arreglo_chocolate1')
        else:
            print('no es valido')
    context = {'form1': form1}
    return render(request, 'arreglo_chocolate.html', context)


@allowed_users(allowed_roles=['administrador'])
def crear_arreglo_chocolate1(request):
    form2 = CrearChocolate()
    if request.method == 'POST':
        form2 = CrearChocolate(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect('arreglo_chocolate2')
        else:
            print('no es valido')
    context = {'form2': form2}
    return render(request, 'arreglo_chocolate1.html', context)


@allowed_users(allowed_roles=['administrador'])
def crear_arreglo_chocolate2(request):
    form3 = CrearArregloChocolates()
    if request.method == 'POST':
        form3 = CrearArregloChocolates(request.POST)
        if form3.is_valid():
            form3.save()
            return redirect('administrador')
        else:
            print('no es valido')
    context = {'form3': form3}
    return render(request, 'arreglo_chocolate2.html', context)


@allowed_users(allowed_roles=['administrador'])
def crear_arreglo_goma(request):
    form = CrearProducto()
    if request.method == 'POST':
        form = CrearProducto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('arreglo_goma1')
        else:
            print('no es valido')
    context = {'form': form}
    return render(request, 'arreglo_goma.html', context)


@allowed_users(allowed_roles=['administrador'])
def crear_arreglo_goma1(request, pk):
    form = CrearGoma()
    if request.method == 'POST':
        form = CrearGoma(request.POST)
        if form.is_valid():
            form.save()
            return redirect('arreglo_goma2')
        else:
            print('no es valido')
    context = {'form': form}
    return render(request, 'arreglo_goma1.html', context)


@allowed_users(allowed_roles=['administrador'])
def crear_arreglo_goma2(request):
    form = CrearArreglogoma()
    if request.method == 'POST':
        form = CrearArreglogoma(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administrador')
        else:
            print('no es valido')
    context = {'form': form}
    return render(request, 'arreglo_goma2.html', context)


@allowed_users(allowed_roles=['administrador'])
def crear_caja_chocolate(request):
    form = CrearProducto()
    if request.method == 'POST':
        form = CrearProducto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('caja_chocolate1')
        else:
            print('no es valido')
    context = {'form': form}
    return render(request, 'caja_chocolate.html', context)


def crear_caja_chocolate1(request):
    form = CrearChocolate()
    if request.method == 'POST':
        form = CrearChocolate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('caja_chocolate2')
        else:
            print('no es valido')
    context = {'form': form}
    return render(request, 'caja_chocolate1.html', context)


def crear_caja_chocolate2(request):
    form = CrearCajaChocolates()
    if request.method == 'POST':
        form = CrearCajaChocolates(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administrador')
        else:
            print('no es valido')
    context = {'form': form}
    return render(request, 'caja_chocolate2.html', context)


@allowed_users(allowed_roles=['administrador'])
def crear_caja_goma(request):
    form = CrearProducto()
    if request.method == 'POST':
        form = CrearProducto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('caja_goma1')
        else:
            print('no es valido')
    context = {'form': form}
    return render(request, 'caja_goma.html', context)


@allowed_users(allowed_roles=['administrador'])
def crear_caja_goma1(request):
    form = CrearGoma()
    if request.method == 'POST':
        form = CrearGoma(request.POST)
        if form.is_valid():
            form.save()
            return redirect('caja_goma2')
        else:
            print('no es valido')
    context = {'form': form}
    return render(request, 'caja_goma1.html', context)


@allowed_users(allowed_roles=['administrador'])
def crear_caja_goma2(request):
    form = CrearCajaGomas()
    if request.method == 'POST':
        form = CrearCajaGomas(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administrador')
        else:
            print('no es valido')
    context = {'form': form}
    return render(request, 'caja_goma2.html', context)


@allowed_users(allowed_roles=['administrador'])
def crear_flor(request):
    form = CrearProducto()
    if request.method == 'POST':
        form = CrearProducto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flor1')
        else:
            print('no es valido')
    context = {'form': form}
    return render(request, 'flor.html', context)


@allowed_users(allowed_roles=['administrador'])
def crear_flor1(request):
    form = CrearFlores()
    if request.method == 'POST':
        form = CrearFlores(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administrador')
        else:
            print('no es valido')
    context = {'form': form}
    return render(request, 'flor1.html', context)


def actualizar(request, pk):
    producto = Producto.objects.get(id_producto=pk)
    form = CrearProducto(instance=producto)
    try:
        ArregloGoma.objects.get(id_producto=pk)
        if request.method == 'POST':
            form = CrearProducto(request.POST, instance=producto)
            if form.is_valid():
                form.save()
                return redirect('administrador')
        context = {'form': form}
        return render(request, 'arreglo_goma.html', context)
    except:
        pass
    try:
        CajaGoma.objects.get(id_producto=pk)
        if request.method == 'POST':
            form = CrearProducto(request.POST, instance=producto)
            if form.is_valid():
                form.save()
                return redirect('administrador')
        context = {'form': form}
        return render(request, 'caja_goma.html', context)
    except:
        pass
    try:
        ArregloChocolate.objects.get(id_producto=pk)
        if request.method == 'POST':
            form = CrearProducto(request.POST, instance=producto)
            if form.is_valid():
                form.save()
                return redirect('administrador')
        context = {'form': form}
        return render(request, 'arreglo_chocolate.html', context)
    except:
        pass
    try:
        CajaChocolate.objects.get(id_producto=pk)
        if request.method == 'POST':
            form = CrearProducto(request.POST, instance=producto)
            if form.is_valid():
                form.save()
                return redirect('administrador')
        context = {'form': form}
        return render(request, 'caja_chocolate.html', context)
    except:
        pass
    try:
        Flor.objects.get(id_producto=pk)
        if request.method == 'POST':
            form = CrearProducto(request.POST, instance=producto)
            if form.is_valid():
                form.save()
                return redirect('administrador')
        context = {'form': form}
        return render(request, 'flor.html', context)
    except:
        pass


def eliminar(request, pk):
    producto = Producto.objects.get(id_producto=pk)
    producto.delete()
    return redirect('administrador')

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