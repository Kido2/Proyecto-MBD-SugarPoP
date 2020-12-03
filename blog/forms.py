from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from blog.models import *


class InfoCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'documento',
            'pais',
            'ciudad',
            'direccion',
            'telefono',
            'id_user',
        ]

        labels = {
            'documento': 'Documento',
            'pais': 'País',
            'ciudad': 'Ciudad',
            'direccion': 'Dirección',
            'telefono': 'Telefono',
            'id_user': 'User',
        }


class CrearProducto(ModelForm):
    class Meta:
        model = Producto
        fields = [
            'id_producto',
            'nombre',
            'precio',
            'imagen',
            'documento_admin'
        ]


class CrearChocolate(ModelForm):
    class Mete:
        model = Chocolate
        fields = [
            'id_producto',
            'sabor',
            'tipo'
        ]


class CrearGoma(ModelForm):
    class Mete:
        model = Chocolate
        fields = [
            'id_producto',
            'sabor',
            'tipo'
        ]


class CrearCajaChocolates(ModelForm):
    class Meta:
        model = CajaChocolate
        fields = [
            'id_producto',
            'categoria',
            'peso',
            'expedicion',
            'expiracion',
            'precio',
            'unidades'
        ]


class CrearCajaGomas(ModelForm):
    class Meta:
        model = CajaGoma
        fields = [
            'id_producto',
            'categoria',
            'peso',
            'expedicion',
            'expiracion',
            'precio',
            'unidades'
        ]


class CrearArregloChocolates(ModelForm):
    class Meta:
        model = ArregloChocolate
        fields = [
            'id_producto',
            'tema',
            'expedicion',
            'peso',
            'empaque'
        ]


class CrearArreglogoma(ModelForm):
    class Meta:
        model = ArregloGoma
        fields = [
            'id_producto',
            'tema',
            'expedicion',
            'peso',
            'empaque'
        ]


class CrearFlores(ModelForm):
    class Meta:
        model = Flor
        fields = [
            'id_producto',
            'peso',
            'cantidad'
        ]
