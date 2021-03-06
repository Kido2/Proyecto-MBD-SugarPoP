import datetime
import os
from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import *

admin.site.register([Admin, Producto, Domiciliario, Cliente, MetodoDePago, Factura, CarritoCompra, ProductoCarrito,
                     ClienteCarrito, ClienteCarritoFactura, Goma, Chocolate, Flor, CajaChocolate, CajaGoma, ArregloGoma,
                     ArregloChocolate])

################################################################################################################################
admin.site.register(Order)
admin.site.register(OrderItem)
################################################################################################################################


# Iniciar datos

a1 = Admin(documento=1085987365, id_user_id=1)
a1.save()

pc1 = Producto(id_producto=1, nombre='Caja de Chocolates Picantes', precio=8300, imagen='picantechoc.png', documento_admin_id=1085987365)
pc1.save()
cp1 = Chocolate(id_producto_id=1, sabor='picante', tipo='artesanos')
cp1.save()
c1 = CajaChocolate(id_producto_id=1, categoria='artesano', peso=234, expedicion=datetime.date(2020, 7, 17),
                   expiracion=datetime.date(2021, 7, 10), unidades=10)
c1.save()

pc2 = Producto(id_producto=2, nombre='Caja de Chocolates Blancos', precio=10400,imagen='cajablancos.png', documento_admin_id=1085987365)
pc2.save()
cp2 = Chocolate(id_producto_id=2, sabor='leche', tipo='blancos', )
cp2.save()
c2 = CajaChocolate(id_producto_id=2, categoria='blanco', peso=218, expedicion=datetime.date(2020, 9, 23),
                   expiracion=datetime.date(2021, 9, 21), unidades=13)
c2.save()

pc3 = Producto(id_producto=3, nombre='Caja de Chocolates Baileys', precio=17200,imagen='cjabaileys.png',documento_admin_id=1085987365)
pc3.save()
cp3 = Chocolate(id_producto_id=3, sabor='baileys', tipo='rellenos')
cp3.save()
c3 = CajaChocolate(id_producto_id=3, categoria='relleno', peso=357, expedicion=datetime.date(2020, 4, 26),
                   expiracion=datetime.date(2021, 2, 24), unidades=12)
c3.save()

pc4 = Producto(id_producto=4, nombre='Caja de Chocolate de Mojito', precio=6800,imagen='cajamojito.png', documento_admin_id=1085987365)
pc4.save()
cp4 = Chocolate(id_producto_id=4, sabor='mojito', tipo='negros')
cp4.save()
c4 = CajaChocolate(id_producto_id=4, categoria='negro', peso=278, expedicion=datetime.date(2020, 10, 8),
                   expiracion=datetime.date(2020, 9, 11), unidades=17)
c4.save()

pc5 = Producto(id_producto=5, nombre='Arreglo de chocolates Anchoas', precio=23500,imagen='arregloanchoas.png', documento_admin_id=1085987365)
pc5.save()
cp5 = Chocolate(id_producto_id=5, sabor='anchoa', tipo='artesanos')
cp5.save()
c5 = ArregloChocolate(id_producto_id=5, tema='Amor y amistad',expedicion=datetime.date(2020, 2, 19),peso=1000, empaque='estuche')
c5.save()

pc6 = Producto(id_producto=6, nombre='Arreglo de Chocolates Citrus ', precio=14800,imagen='choclcit.png', documento_admin_id=1085987365)
pc6.save()
cp6 = Chocolate(id_producto_id=6, sabor='naranja', tipo='trufas')
cp6.save()
c6 = ArregloChocolate(id_producto_id=6, tema='Dia de las madres', expedicion=datetime.date(2020, 3, 25),peso=1500, empaque='caja')
c6.save()

pc7 = Producto(id_producto=7, nombre='Arreglo de Chocolates de Coco', precio=19900,imagen='arreglococo.png',documento_admin_id=1085987365)
pc7.save()
cp7 = Chocolate(id_producto_id=7, sabor='coco', tipo='rellenos')
cp7.save()
c7 = ArregloChocolate(id_producto_id=7, tema='Amigo secreto',expedicion=datetime.date(2020, 4, 29),peso=1250, empaque='bolsa')
c7.save()

# GOMITAS
pg1 = Producto(id_producto=8, nombre='Caja de Corazoncitos', precio=7500,imagen='corazon.png' ,documento_admin_id=1085987365)
pg1.save()
gp1 = Goma(id_producto_id=8, sabor='Fresa', tipo='Corazones')
gp1.save()
g1 = CajaGoma(id_producto_id=8, categoria='Corazon', peso=500, expedicion=datetime.date(2020, 11, 7),
              expiracion=datetime.date(2021, 11, 7), unidades=30)
g1.save()

pg2 = Producto(id_producto=9, nombre='Cajita Egipto', precio=360, imagen='priamidescaj.png',documento_admin_id=1085987365)
pg2.save()
gp2 = Goma(id_producto_id=9, sabor='Surtido', tipo='Piramides')
gp2.save()
g2 = CajaGoma(id_producto_id=9, categoria='Piramide', peso=8900, expedicion=datetime.date(2020, 10, 7),
              expiracion=datetime.date(2021, 10, 7), unidades=25)
g2.save()

pg3 = Producto(id_producto=10, nombre='Cajita Rellenitos', precio=10000, imagen='choc.png',documento_admin_id=1085987365)
pg3.save()
gp3 = Goma(id_producto_id=10, sabor='Surtido', tipo='Relleno_chocolate')
gp3.save()
g3 = CajaGoma(id_producto_id=10, categoria='Relleno_chc', peso=1000,
              expedicion=datetime.date(2020, 8, 10),
              expiracion=datetime.date(2021, 8, 10), unidades=30)
g3.save()

pg4 = Producto(id_producto=11, nombre='Cajita Selvatica', precio=15000,imagen='serpientes.png' ,documento_admin_id=1085987365)
pg4.save()
gp4 = Goma(id_producto_id=11, sabor='Limon', tipo='Serpientes')
gp4.save()
g4 = CajaGoma(id_producto_id=11, categoria='Serpiente', peso=1000, expedicion=datetime.date(2020, 11, 7),
              expiracion=datetime.date(2021, 11, 7), unidades=15)
g4.save()

pg5 = Producto(id_producto=12, nombre='Cajita Cintas de sandia', precio=37000,imagen='cinta.png', documento_admin_id=1085987365)
pg5.save()
gp5 = Goma(id_producto_id=12, sabor='Sandia', tipo='Cintas')
gp5.save()
g5 = CajaGoma(id_producto_id=12, categoria='Cintas', peso=700, expedicion=datetime.date(2020, 10, 10),
              expiracion=datetime.date(2021, 10, 10), unidades=120)
g5.save()

pg6 = Producto(id_producto=13, nombre='Arreglo Ositos', precio=35000,imagen='ositos.png', documento_admin_id=1085987365)
pg6.save()
gp6 = Goma(id_producto_id=13, sabor='Piña', tipo='Ositos')
gp6.save()
g6 = ArregloGoma(id_producto_id=13, tema='Verano', expedicion=datetime.date(2021, 10, 10),
                 peso=1000, empaque='Canasta')
g6.save()

pg7 = Producto(id_producto=14, nombre='Arreglo Aritos', precio=40000, imagen='rana.png', documento_admin_id=1085987365)
pg7.save()
gp7 = Goma(id_producto_id=14, sabor='Mora', tipo='aros')
gp7.save()
g7 = ArregloGoma(id_producto_id=14, tema='Halloween', expedicion=datetime.date(2021, 10, 10), peso=4000,
                 empaque='Bolsa')
g7.save()

pg8 = Producto(id_producto=15, nombre='Arreglo coco', precio=37500,imagen='coco.png', documento_admin_id=1085987365)
pg8.save()
gp8 = Goma(id_producto_id=15, sabor='Coco', tipo='Ositos')
gp8.save()
g8 = ArregloGoma(id_producto_id=15, tema='Navidad', expedicion=datetime.date(2021, 10, 10)
                 , peso=4000, empaque='Canasta')
g8.save()

# FLORES
pf1 = Producto(id_producto=16, nombre='Ramo de rosas', precio=26000,imagen='ramorosas.png', documento_admin_id=1085987365)
pf1.save()
f1 = Flor(id_producto_id=16, peso=6000, cantidad=12)
f1.save()

pf2 = Producto(id_producto=17, nombre='Ramo de girasoles', precio=50000,imagen='girasoles.png', documento_admin_id=1085987365)
pf2.save()
f2 = Flor(id_producto_id=17, peso=9000, cantidad=6)
f2.save()

pf3 = Producto(id_producto=18, nombre='Ramo de flores mixto', precio=60000,imagen='ramomix.png', documento_admin_id=1085987365)
pf3.save()
f3 = Flor(id_producto_id=18, peso=6000, cantidad=17)
f3.save()

pf4 = Producto(id_producto=19, nombre='Caja de rosas', precio=75000,imagen='cajarosas.png', documento_admin_id=1085987365)
pf4.save()
f4 = Flor(id_producto_id=19, peso=12000, cantidad=24)
f4.save()

pf5 = Producto(id_producto=20, nombre='Caja de flores mixta', precio=68000, imagen='cajaflores.png',documento_admin_id=1085987365)
pf5.save()
f5 = Flor(id_producto_id=19, peso=12000   , cantidad=24)
f5.save()
