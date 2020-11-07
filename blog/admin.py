from django.contrib import admin
from .models import Admin, User_sugar, Product, Domc, Client

admin.site.register([Admin, User_sugar, Product, Domc, Client])
