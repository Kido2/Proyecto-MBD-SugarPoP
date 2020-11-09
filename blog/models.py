from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
# class Post(models.Model):
#     STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'),)
#     title = models.CharField(max_length=250)
#     slug = models.SlugField(max_length=250, unique_for_date='publish')
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
#     body = models.TextField()
#     publish = models.DateTimeField(default=timezone.now)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
#
#     class Meta:
#         ordering = ('-publish',)
#
#     def __str__(self):
#         return self.title


class User_sugar(models.Model):
    id_user = models.SmallIntegerField(primary_key=True)
    nickname = models.CharField(max_length=60)
    password = models.CharField(max_length=60)

    def __str__(self):
        return "{0}".format(self.id_user)


class Admin(models.Model):
    document = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    id_user = models.OneToOneField(
        User_sugar,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{0}".format(self.document)


class Client(models.Model):
    document = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    direction = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    phone = models.BigIntegerField(null=False)
    id_user = models.OneToOneField(
        User_sugar,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{0}".format(self.document)


class Method_of_payment(models.Model):
    document = models.ForeignKey(Client, on_delete=models.CASCADE)
    efective = models.BooleanField(null=False)
    credit_card = models.BooleanField(null=False)
    debit_card = models.BooleanField(null=False)

    def __str__(self):
        if self.efective:
            return "%s has as payment method efective" % (self.document)
        elif self.credit_card:
            return "%s has as payment method credit card" % (self.document)
        elif self.debit_card:
            return "%s has as payment method debit card" % (self.document)
        else:
            return "%s doesnt have a payment method" % (self.document)


class Domc(models.Model):
    document = models.BigIntegerField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    direction = models.CharField(max_length=50)
    id_user = models.OneToOneField(
        User_sugar,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{0}".format(self.document)


class Fact(models.Model):
    id_fact = models.SmallIntegerField(primary_key=True)
    document_client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
    )
    date_of_expedition = models.DateTimeField(default=timezone.now)
    num_item = models.SmallIntegerField(null=False)
    document_domc = models.ForeignKey(Domc,on_delete=models.CASCADE)

    def __str__(self):
        return "{0}".format(self.id_fact)


class Product(models.Model):
    id_product = models.SmallIntegerField(primary_key=True)
    product_name = models.CharField(null=False, max_length=50)
    unit_price = models.IntegerField(null=False)
    document_admin = models.ForeignKey(
        Admin,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{0}".format(self.id_product)


class Shopping_cart(models.Model):
    id_cart = models.SmallIntegerField(primary_key=True)
    quantity = models.SmallIntegerField(null=False)
    total_price = models.IntegerField(null=False)
    date_of_validation = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{0}".format(self.id_cart)


class Product_cart(models.Model):
    id_cart = models.ForeignKey(Shopping_cart, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return "In the cart %s is the product %s" % (self.id_cart, self.id_product)


class Client_cart(models.Model):
    document_client = models.OneToOneField(Client, on_delete=models.CASCADE, default=0)
    id_shopping_cart = models.OneToOneField(Shopping_cart, on_delete=models.CASCADE)

    def __str__(self):
        return "%s client has %s shopping cart" % (self.document_client, self.id_shopping_cart)


class Client_cartfac(models.Model):
    id_fact = models.OneToOneField(Fact, on_delete=models.CASCADE)
    id_cart = models.OneToOneField(Shopping_cart, on_delete=models.CASCADE)

    def __str__(self):
        return "The invoice %s belongs to the cart %s" % (self.id_fact, self.id_cart)


class Gummy(models.Model):
    id_product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    flavor = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def __str__(self):
        return "{0}".format(self.id_product)


class Chocolate(models.Model):
    id_product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    flavor = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def __str__(self):
        return "{0}".format(self.id_product)


class Flowers(models.Model):
    id_product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    weight = models.SmallIntegerField(null=False)
    price_of_bouquet = models.IntegerField(null=False)
    amount_of_flowers = models.SmallIntegerField(null=False)

    def __str__(self):
        return "{0}".format(self.id_product)


class Box_of_chocolates(models.Model):
    id_product = models.OneToOneField(
        Chocolate,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    category = models.CharField(max_length=30)
    weight = models.SmallIntegerField(null=False)
    expedition_date = models.DateTimeField(default=timezone.now)
    expiration_date = models.DateTimeField(default=timezone.now)
    total_price = models.IntegerField(null=False)
    number_of_units = models.SmallIntegerField(null=False)

    def __str__(self):
        return "{0}".format(self.id_product)


class Box_of_gummies(models.Model):
    id_product = models.OneToOneField(
        Gummy,
        on_delete=models.CASCADE,
        primary_key=True
    )
    category = models.CharField(max_length=30)
    weight = models.SmallIntegerField(null=False)
    expedition_date = models.DateTimeField(default=timezone.now)
    expiration_date = models.DateTimeField(default=timezone.now)
    total_price = models.IntegerField(null=False)
    number_of_units = models.SmallIntegerField(null=False)

    def __str__(self):
        return "{0}".format(self.id_product)


class Arrag_of_gummies(models.Model):
    id_product = models.ForeignKey(
        Gummy,
        on_delete=models.CASCADE,
        primary_key=True
    )
    arrag_price = models.IntegerField(null=False)
    theme = models.CharField(max_length=50)
    expedition_date = models.DateTimeField(default=timezone.now)
    weight = models.SmallIntegerField(null=False)
    package = models.CharField(max_length=50)

    def __str__(self):
        return "{0}".format(self.id_product)


class Arrag_of_chocls(models.Model):
    id_product = models.ForeignKey(
        Chocolate,
        on_delete=models.CASCADE,
        primary_key=True
    )
    arrag_price = models.IntegerField(null=False)
    theme = models.CharField(max_length=50)
    expedition_date = models.DateTimeField(default=timezone.now)
    weight = models.SmallIntegerField(null=False)
    package = models.CharField(max_length=50)

    def __str__(self):
        return "{0}".format(self.id_product)
