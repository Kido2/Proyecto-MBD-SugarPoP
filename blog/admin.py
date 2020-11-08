from django.contrib import admin
from .models import Admin, User_sugar, Product, Domc, Client, Method_of_payment, Fact, Shopping_cart, Product_cart, \
    Client_cart, Client_cartfac, Gummy, Chocolate, Flowers, Box_of_chocolates, Box_of_gummies, Arrag_of_gummies, \
    Arrag_of_chocls

admin.site.register([User_sugar, Admin, Client, Admin, User_sugar, Product, Domc, Client, Method_of_payment, Fact, 
                     Shopping_cart, Product_cart, Client_cart, Client_cartfac, Gummy, Chocolate, Flowers, 
                     Box_of_chocolates, Box_of_gummies, Arrag_of_gummies, Arrag_of_chocls])

u1 = User_sugar(id_user=1, nickname='Nico', password='Nicoolas_123')
u1.save()

