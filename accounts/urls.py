from django.urls import path
from . import views

urlpatterns = [
    path('registrar_cliente/', views.registrar_cliente, name="registrar_cliente"),
    path('registrar_domiciliario/', views.registrar_domiciliario, name="registrar_domiciliario"),
    path('role/', views.role, name="role"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]