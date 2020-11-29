import datetime
import os
from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Admin, Producto, Domciliario, Cliente, MetodoDePago, Factura, CarritoCompra, ProductoCarrito, \
    ClienteCarrito, ClienteCarritoFactura, Goma, Chocolate, Flor, CajaChocolate, CajaGoma, ArregloGoma, \
    ArregloChocolate

admin.site.register([Admin, Producto, Domciliario, Cliente, MetodoDePago, Factura, CarritoCompra, ProductoCarrito,
                     ClienteCarrito, ClienteCarritoFactura, Goma, Chocolate, Flor, CajaChocolate, CajaGoma, ArregloGoma,
                     ArregloChocolate])
