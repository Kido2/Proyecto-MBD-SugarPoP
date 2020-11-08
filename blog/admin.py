from django.contrib import admin
from .models import Admin, User_sugar, Product, Domc, Client

admin.site.register([Admin, User_sugar, Product, Domc, Client])

u1 = User_sugar(id_user=1, nickname='Nico', password='Nicoolas_123')
u1.save()
