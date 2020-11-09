import datetime
import os
from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Admin, User_sugar, Product, Domc, Client, Method_of_payment, Fact, Shopping_cart, Product_cart, \
    Client_cart, Client_cartfac, Gummy, Chocolate, Flowers, Box_of_chocolates, Box_of_gummies, Arrag_of_gummies, \
    Arrag_of_chocls

admin.site.register([User_sugar, Admin, Product, Domc, Client, Method_of_payment, Fact,
                     Shopping_cart, Product_cart, Client_cart, Client_cartfac, Gummy, Chocolate, Flowers,
                     Box_of_chocolates, Box_of_gummies, Arrag_of_gummies, Arrag_of_chocls])

# Cambiar direccion de carpeta migrations
if os.path.isdir('~/Universidad/Bases_de_datos/Proyecto-MBD-SugarPoP/blog/migrations'):
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

    # Crear los usuarios
    [user.delete() for user in list(User.objects.all())]
    User.objects.create_superuser('admin@sugarpop.com', 'admin@sugarpop.com', 'admin_el_mejor^')
    User.objects.create_user('andres0678@gmail.com', 'andres0678@gmail.com', 'user_21345^')
    User.objects.create_user('gerard17@gmail.com', 'gerard17@gmail.com', 'user_354352^')
    User.objects.create_user('enzo99p@gmail.com', 'enzo99p@gmail.com', 'user_23464^')
    User.objects.create_user('ivan0123@gmail.com', 'ivan0123@gmail.com', 'user_586534^')
    User.objects.create_user('juan5643@gmail.com', 'juan5643@gmail.com', 'user_1234467^')
    User.objects.create_user('nicolas0699@gmail.com', 'nicolas0699@gmail.com', 'user_serr32321^')

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

    # CHOCOLATES
    pc1 = Product(id_product=1, product_name='jalapy_chocolate_box', unit_price=800, document_admin_id=1085987365)
    pc1.save()
    cp1 = Chocolate(id_product_id=1, flavor='picante', type='artesanos')
    cp1.save()
    c1 = Box_of_chocolates(id_product_id=1, category='artesano', weight=234, expedition_date=datetime.date(2020, 7, 17),
                           expiration_date=datetime.date(2021, 7, 10), total_price=8300, number_of_units=10)
    c1.save()

    pc2 = Product(id_product=2, product_name='pasti_white_chocolate_box', unit_price=800, document_admin_id=1085987365)
    pc2.save()
    cp2 = Chocolate(id_product_id=2, flavor='leche', type='blancos', )
    cp2.save()
    c2 = Box_of_chocolates(id_product_id=2, category='blanco', weight=218, expedition_date=datetime.date(2020, 9, 23),
                           expiration_date=datetime.date(2021, 9, 21), total_price=10400, number_of_units=13)
    c2.save()

    pc3 = Product(id_product=3, product_name='baileys__chocolate_box', unit_price=1400, document_admin_id=1085987365)
    pc3.save()
    cp3 = Chocolate(id_product_id=3, flavor='baileys', type='rellenos')
    cp3.save()
    c3 = Box_of_chocolates(id_product_id=3, category='relleno', weight=357, expedition_date=datetime.date(2020, 4, 26),
                           expiration_date=datetime.date(2021, 2, 24), total_price=17.200, number_of_units=12)
    c3.save()

    pc4 = Product(id_product=4, product_name='mojitos_chocolate_box', unit_price=400, document_admin_id=1085987365)
    pc4.save()
    cp4 = Chocolate(id_product_id=4, flavor='mojito', type='negros')
    cp4.save()
    c4 = Box_of_chocolates(id_product_id=4, category='negro', weight=278, expedition_date=datetime.date(2020, 10, 8),
                           expiration_date=datetime.date(2020, 9, 11), total_price=6800, number_of_units=17)
    c4.save()

    pc5 = Product(id_product=5, product_name='anchoas_chocolate_arrangement', unit_price=700,
                  document_admin_id=1085987365)
    pc5.save()
    cp5 = Chocolate(id_product_id=5, flavor='anchoa', type='artesanos')
    cp5.save()
    c5 = Arrag_of_chocls(id_product_id=5, arrag_price=23500, theme='Amor y amistad',
                         expedition_date=datetime.date(2020, 2, 19),
                         weight=1000, package='estuche')
    c5.save()

    pc6 = Product(id_product=6, product_name='citrus_chocolate_arrangement', unit_price=900,
                  document_admin_id=1085987365)
    pc6.save()
    cp6 = Chocolate(id_product_id=6, flavor='naranja', type='trufas')
    cp6.save()
    c6 = Arrag_of_chocls(id_product_id=6, arrag_price=34800, theme='Dia de las madres',
                         expedition_date=datetime.date(2020, 3, 25),
                         weight=1500, package='caja')
    c6.save()

    pc7 = Product(id_product=7, product_name='coco_chocolate_arrangement', unit_price=700, document_admin_id=1085987365)
    pc7.save()
    cp7 = Chocolate(id_product_id=7, flavor='coco', type='rellenos')
    cp7.save()
    c7 = Arrag_of_chocls(id_product_id=7, arrag_price=19900, theme='Amigo secreto',
                         expedition_date=datetime.date(2020, 4, 29),
                         weight=1250, package='bolsa')
    c7.save()

    # GOMITAS
    pg1 = Product(id_product=8, product_name='Corazoncitos', unit_price=250, document_admin_id=1085987365)
    pg1.save()
    gp1 = Gummy(id_product_id=8, flavor='Fresa', type='Corazones')
    gp1.save()
    g1 = Box_of_gummies(id_product_id=8, category='Corazon', weight=500, expedition_date=datetime.date(2020, 11, 7),
                        expiration_date=datetime.date(2021, 11, 7), total_price=7500, number_of_units=30)
    g1.save()

    pg2 = Product(id_product=9, product_name='Egipt', unit_price=360, document_admin_id=1085987365)
    pg2.save()
    gp2 = Gummy(id_product_id=9, flavor='Surtido', type='Piramides')
    gp2.save()
    g2 = Box_of_gummies(id_product_id=9, category='Piramide', weight=800, expedition_date=datetime.date(2020, 10, 7),
                        expiration_date=datetime.date(2021, 10, 7), total_price=8900, number_of_units=25)
    g2.save()

    pg3 = Product(id_product=10, product_name='Rellenitos', unit_price=340, document_admin_id=1085987365)
    pg3.save()
    gp3 = Gummy(id_product_id=10, flavor='Surtido', type='Relleno_chocolate')
    gp3.save()
    g3 = Box_of_gummies(id_product_id=10, category='Relleno_chc', weight=1000,
                        expedition_date=datetime.date(2020, 8, 10),
                        expiration_date=datetime.date(2021, 8, 10), total_price=10000, number_of_units=30)
    g3.save()

    pg4 = Product(id_product=11, product_name='Selva', unit_price=1000, document_admin_id=1085987365)
    pg4.save()
    gp4 = Gummy(id_product_id=11, flavor='Limon', type='Serpientes')
    gp4.save()
    g4 = Box_of_gummies(id_product_id=11, category='Serpiente', weight=1000, expedition_date=datetime.date(2020, 11, 7),
                        expiration_date=datetime.date(2021, 11, 7), total_price=15000, number_of_units=15)
    g4.save()

    pg5 = Product(id_product=12, product_name='Sandicin', unit_price=310, document_admin_id=1085987365)
    pg5.save()
    gp5 = Gummy(id_product_id=12, flavor='Sandia', type='Cintas')
    gp5.save()
    g5 = Box_of_gummies(id_product_id=12, category='Cintas', weight=700, expedition_date=datetime.date(2020, 10, 10),
                        expiration_date=datetime.date(2021, 10, 10), total_price=37000, number_of_units=120)
    g5.save()

    pg6 = Product(id_product=13, product_name='Ossy', unit_price=2600, document_admin_id=1085987365)
    pg6.save()
    gp6 = Gummy(id_product_id=13, flavor='Piña', type='Ositos')
    gp6.save()
    g6 = Arrag_of_gummies(id_product_id=13, arrag_price=35000, theme='Verano', weight=1000, package='Canasta')
    g6.save()

    pg7 = Product(id_product=14, product_name='Saltarin', unit_price=3000, document_admin_id=1085987365)
    pg7.save()
    gp7 = Gummy(id_product_id=14, flavor='Mora', type='Rana')
    gp7.save()
    g7 = Arrag_of_gummies(id_product_id=14, arrag_price=40000, theme='Halloween', weight=4000, package='Bolsa')
    g7.save()

    pg8 = Product(id_product=15, product_name='Coquito', unit_price=1700, document_admin_id=1085987365)
    pg8.save()
    gp8 = Gummy(id_product_id=15, flavor='Coco', type='Ositos')
    gp8.save()
    g8 = Arrag_of_gummies(id_product_id=15, arrag_price=37500, theme='Navidad', weight=4000, package='Canasta')
    g8.save()

    # FLORES
    pf1 = Product(id_product=16, product_name='ramo_rosas', unit_price=2000, document_admin_id=1085987365)
    pf1.save()
    f1 = Flowers(id_product_id=16, weight=6000, price_of_bouquet=26000, amount_of_flowers=12)
    f1.save()

    pf2 = Product(id_product=17, product_name='ramo_girasoles', unit_price=8000, document_admin_id=1085987365)
    pf2.save()
    f2 = Flowers(id_product_id=17, weight=9000, price_of_bouquet=50000, amount_of_flowers=6)
    f2.save()

    pf3 = Product(id_product=18, product_name='ramo_mix', unit_price=10000, document_admin_id=1085987365)
    pf3.save()
    f3 = Flowers(id_product_id=18, weight=6000, price_of_bouquet=60000, amount_of_flowers=17)
    f3.save()

    pf4 = Product(id_product=19, product_name='caja_rosas', unit_price=2000, document_admin_id=1085987365)
    pf4.save()
    f4 = Flowers(id_product_id=19, weight=12000, price_of_bouquet=75000, amount_of_flowers=24)
    f4.save()

    pf5 = Product(id_product=20, product_name='caja_mix', unit_price=10000, document_admin_id=1085987365)
    pf5.save()
    f5 = Flowers(id_product_id=20, weight=10000, price_of_bouquet=67000, amount_of_flowers=24)
    f5.save()
else:
    pass
