from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("cliente/", views.cliente, name="cliente"),
    path("domiciliario/", views.domiciliario, name="domiciliario"),
    path("administrador/", views.administrador, name="administrador"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("perfil_cliente/", views.perfil_cliente, name="perfil_cliente"),
    path("crear_producto/", views.crear_producto, name="crear_producto"),
    path("tipo/", views.tipo, name="tipo"),
    path("arreglo_chocolate/", views.crear_arreglo_chocolate, name="arreglo_chocolate"),
    path("arreglo_goma/", views.crear_arreglo_goma, name="arreglo_goma"),
    path("caja_chocolate/", views.crear_caja_chocolate, name="caja_chocolate"),
    path("caja_goma/", views.crear_caja_goma, name="caja_goma"),
    path("flores/", views.crear_flores, name="flores"),
]