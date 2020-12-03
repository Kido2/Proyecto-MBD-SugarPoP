from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser


class Admin(models.Model):
    documento = models.BigIntegerField(primary_key=True)
    id_user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{0}".format(self.documento)


class Cliente(models.Model):
    documento = models.BigIntegerField(primary_key=True)
    pais = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    telefono = models.BigIntegerField(null=False)
    id_user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{0}".format(self.documento)


class MetodoDePago(models.Model):
    documento = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    efectivo = models.BooleanField(null=False)
    credito = models.BooleanField(null=False)
    debito = models.BooleanField(null=False)

    def __str__(self):
        return self.documento


class Domiciliario(models.Model):
    documento = models.BigIntegerField(primary_key=True)
    direccion = models.CharField(max_length=50)
    id_user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{0}".format(self.documento)


class Factura(models.Model):
    id_factura = models.SmallIntegerField(primary_key=True)
    documento_cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
    )
    expedicion = models.DateTimeField(default=timezone.now)
    item = models.SmallIntegerField(null=False)
    documento_domiciliario = models.ForeignKey(Domiciliario, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}".format(self.id_factura)


class Producto(models.Model):
    id_producto = models.SmallIntegerField(primary_key=True)
    nombre = models.CharField(null=False, max_length=50)
    precio = models.IntegerField(null=False)
    imagen = models.ImageField(null=True, blank=True)
    documento_admin = models.ForeignKey(
        Admin,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{0}".format(self.id_producto)

    @property
    def imageURL(self):
        try:
            url = self.imagen.url
        except:
            url = ''
        return url


class CarritoCompra(models.Model):
    id_carrito = models.SmallIntegerField(primary_key=True)
    cantidad = models.SmallIntegerField(null=False)
    precio_total = models.IntegerField(null=False)
    validacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{0}".format(self.id_carrito)


class ProductoCarrito(models.Model):
    id_carrito = models.ForeignKey(CarritoCompra, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_carrito, self.id_producto


class ClienteCarrito(models.Model):
    documento_cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, default=0)
    id_carrito_compra = models.OneToOneField(CarritoCompra, on_delete=models.CASCADE)

    def __str__(self):
        return self.documento_cliente, self.id_carrito_compra


class ClienteCarritoFactura(models.Model):
    id_factura = models.OneToOneField(Factura, on_delete=models.CASCADE)
    id_carrito = models.OneToOneField(CarritoCompra, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_factura, self.id_carrito


class Goma(models.Model):
    id_producto = models.OneToOneField(Producto, on_delete=models.CASCADE, primary_key=True)
    sabor = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return "{0}".format(self.id_producto)


class Chocolate(models.Model):
    id_producto = models.OneToOneField(Producto, on_delete=models.CASCADE, primary_key=True)
    sabor = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return "{0}".format(self.id_producto)


class Flor(models.Model):
    id_producto = models.OneToOneField(Producto, on_delete=models.CASCADE, primary_key=True)
    peso = models.SmallIntegerField(null=False)
    cantidad = models.SmallIntegerField(null=False)

    def __str__(self):
        return "{0}".format(self.id_producto)


class CajaChocolate(models.Model):
    id_producto = models.OneToOneField(
        Chocolate,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    categoria = models.CharField(max_length=30)
    peso = models.SmallIntegerField(null=False)
    expedicion = models.DateTimeField(default=timezone.now)
    expiracion = models.DateTimeField(default=timezone.now)
    unidades = models.SmallIntegerField(null=False)

    def __str__(self):
        return "{0}".format(self.id_producto)


class CajaGoma(models.Model):
    id_producto = models.OneToOneField(
        Goma,
        on_delete=models.CASCADE,
        primary_key=True
    )
    categoria = models.CharField(max_length=30)
    peso = models.SmallIntegerField(null=False)
    expedicion = models.DateTimeField(default=timezone.now)
    expiracion = models.DateTimeField(default=timezone.now)
    unidades = models.SmallIntegerField(null=False)

    def __str__(self):
        return "{0}".format(self.id_producto)


class ArregloGoma(models.Model):
    id_producto = models.ForeignKey(
        Goma,
        on_delete=models.CASCADE,
        primary_key=True
    )
    tema = models.CharField(max_length=50)
    expedicion = models.DateTimeField(default=timezone.now)
    peso = models.SmallIntegerField(null=False)
    empaque = models.CharField(max_length=50)

    def __str__(self):
        return "{0}".format(self.id_producto)


class ArregloChocolate(models.Model):
    id_producto = models.ForeignKey(
        Chocolate,
        on_delete=models.CASCADE,
        primary_key=True
    )
    tema = models.CharField(max_length=50)
    expedicion = models.DateTimeField(default=timezone.now)
    peso = models.SmallIntegerField(null=False)
    empaque = models.CharField(max_length=50)

    def __str__(self):
        return "{0}".format(self.id_producto)
