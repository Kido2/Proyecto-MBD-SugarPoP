from django.contrib import admin
from django.contrib.auth.models import User
from .models import Admin, User_sugar, Product, Domc, Client, Method_of_payment, Fact, Shopping_cart, Product_cart, \
    Client_cart, Client_cartfac, Gummy, Chocolate, Flowers, Box_of_chocolates, Box_of_gummies, Arrag_of_gummies, \
    Arrag_of_chocls

admin.site.register([User_sugar, Admin, Product, Domc, Client, Method_of_payment, Fact,
                     Shopping_cart, Product_cart, Client_cart, Client_cartfac, Gummy, Chocolate, Flowers,
                     Box_of_chocolates, Box_of_gummies, Arrag_of_gummies, Arrag_of_chocls])

# Usuarios
u1 = User_sugar(id_user=1, nickname='admin@sugarpop.com', password='admin_el_mejor^')
u2 = User_sugar(id_user=2, nickname='andres0678@gmail.com', password='user_21345^')
u3 = User_sugar(id_user=3, nickname='gerard17@gmail.com', password='user_354352^')
u4 = User_sugar(id_user=4, nickname='enzo99p@gmail.com', password='user_23464^')
u5 = User_sugar(id_user=5, nickname='ivan0123@gmail.com', password='user_586534^')
u6 = User_sugar(id_user=6, nickname='juan5643@gmail.com', password='user_1234467^')
u7 = User_sugar(id_user=7, nickname='hugo634@gmail.com', password='user_90492^')
u8 = User_sugar(id_user=8, nickname='mar54678@gmail.com', password='user_q32043^')
u9 = User_sugar(id_user=9, nickname='nora4234568@gmail.com', password='user_q2iridv^')
u10 = User_sugar(id_user=10, nickname='Sara6708@gmail.com', password='user_q340054^')
u11 = User_sugar(id_user=11, nickname='ulises4563@gmail.com', password='user_23431p30^')
u12 = User_sugar(id_user=12, nickname='nicolas0699@gmail.com', password='user_serr32321^')
u13 = User_sugar(id_user=13, nickname='sofia03456@gmail.com', password='user_2werwer3^')
u14 = User_sugar(id_user=14, nickname='carlos901233@gmail.com', password='user_32425^')
u15 = User_sugar(id_user=15, nickname='juan4325@gmail.com', password='user_029034jf^')
u16 = User_sugar(id_user=16, nickname='marta21086@gmail.com', password='user_ew0r95432^')

u1.save()
u2.save()
u3.save()
u4.save()
u5.save()
u6.save()
u7.save()
u8.save()
u9.save()
u10.save()
u11.save()
u12.save()
u13.save()
u14.save()
u15.save()
u16.save()

# Clientes
t1 = Client(document=1085345780, name='Andrés Cristiano Gonzales López', country='Colombia', city='Bogotá',
            direction='La Candelaria', email='andres0678@gmail.com', phone=3172159870, id_user_id=2)

t2 = Client(document=10852354782, name='Gerard Lionel Díaz Martínez', country='Colombia', city='Bogota',
            direction='cll primavera', email='gerard17@gmail.com', phone=3132154850, id_user_id=3)

t3 = Client(document=123435547, name='Enzo Cristiano Torres López', country='Colombia', city='Bogota',
            direction='Cll 19', email='enzo99p@gmail.com', phone=3172093470, id_user_id=4)

t4 = Client(document=23465121, name='Iván Cristiano Gonzales Romero', country='Colombia', city='Bogota',
            direction='Portal 80', email='ivan0123@gmail.com', phone=3177654870, id_user_id=5)

t5 = Client(document=12457542, name='Juan Cristiano Flores López', country='Colombia', city='Bogota',
            direction='Campin', email='juan5643@gmail.com', phone=3154329870, id_user_id=6)

t6 = Client(document=123435546, name='Hugo Cristiano Gonzales Suárez', country='Colombia', city='Bogota',
            direction='cra 30 # 30-30', email='hugo634@gmail.com', phone=3172432870, id_user_id=7)

t7 = Client(document=234357654, name='Mar Eva Aguirre López', country='Colombia', city='Bogota',
            direction='El Bronx', email='mar54678@gmail.com', phone=3154335678, id_user_id=8)

t8 = Client(document=234467542, name='Nora Gonzales Sosa', country='Colombia', city='Bogota',
            direction='Villa luz', email='nora4234568@gmail.com', phone=3165459870, id_user_id=9)

t9 = Client(document=123467533, name='Sara Gómez López', country='Colombia', city='Bogota',
            direction='Suba', email='Sara6708@gmail.com', phone=3172151230, id_user_id=10)

t10 = Client(document=346542353, name='Ulises Cristiano Gonzales Ruiz', country='Colombia', city='Bogota',
             direction='Kennedy', email='Ulises9393@gmail.com', phone=31721592370, id_user_id=11)

t1.save()
t2.save()
t3.save()
t4.save()
t5.save()
t6.save()
t7.save()
t8.save()
t9.save()
t10.save()

# Administrador
a1 = Admin(document=1085987365, name='Thor Spartaco Domínguez Carrizo', email='admin@sugarpop.com', id_user_id=1)
a1.save()

# Domiciliarios

d1 = Domc(document=1698745610, name='Nicolas Caicedo', direction='Kennedy', id_user_id=12)
d2 = Domc(document=1698123610, name='Sofia Robayo', direction='Villa luz', id_user_id=13)
d3 = Domc(document=16948532610, name='Carlos Muñoz', direction='Campin', id_user_id=14)
d4 = Domc(document=1698740386, name='Juan Rodriguez', direction='El Bronx', id_user_id=15)
d5 = Domc(document=1698710488, name='Marta Marcapasos', direction='Suba', id_user_id=16)

d1.save()
d2.save()
d3.save()
d4.save()
d5.save()
