from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("cliente/", views.cliente, name="cliente"),
    path("domiciliario/", views.domiciliario, name="domiciliario"),
    path("administrador/", views.administrador, name="administrador"),
]