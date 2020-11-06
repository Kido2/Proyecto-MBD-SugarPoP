from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'),)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class user(models.Model):
    id_user = models.SmallIntegerField(primary_key=True)
    nickname = models.CharField(60)
    password = models.CharField(60)

    def __str__(self):
        return "%s is the identification of user %s" % (self.id_user, self.nickname)


class admin(models.Model):
    id_admin = models.SmallIntegerField(primary_key=True)
    name = models.CharField(50)
    id = models.SmallIntegerField(null=False)
    email = models.CharField(30)

    def __str__(self):
        return "%s is the admin" % self.name


class client(models.Model):
    id_client = models.IntegerField(primary_key=True)
    name= models.CharField(50)
    country= models.CharField(20)
    city = models.CharField(20)
    direction=models.CharField(50)
    email= models.CharField(30)
    phone=models.SmallIntegerField(null=False)
    id_user= models.OneToOneField(
    user,
    on_delete = models.CASCADE,
    )

    def __str__(self):
        return "%s has ID as %s"%(self.name, self.id_client)


class method_of_payment(models.Model):
    document_client = models.ForeignKey(client, on_delete=models.CASCADE)
    efective = models.BooleanField(null=False)
    credit_card = models.BooleanField(null=False)
    debit_card = models.BooleanField(null=False)

    def __str__(self):
        if efective == True:
            return "%s has as payment method %s"(self.document_client, self.efective)
        elif credit_card == True:
            return "%s has as payment method %s"(self.document_client, self.credit_card)
        elif debit_card == True:
            return "%s has as payment method %s"(self.document_client, self.debit_card)
        else:
            return "%s doesnt have a payment method %s"(self.document_client)


class fact(models.Model):
    id_fact = models.SmallIntegerField(primary_key=True)
    id_client = models.SmallIntegerField(null=False)
    d_o_exp= models.DateTimeField(default=timezone.now)
    num_item= models.SmallIntegerField(null=False)

    def __str__(self):
        return "%s client has %s facture"%(self.id_client, self.id_fact)


class domc(models.Model):
    id_domc = models.OneToOneField(
    user,
    on_delete=models.CASCADE,
    primary_key=True

    )
    name=models.CharField(50)
    id_fact=models.ForeignKey(fact, on_delete=models.CASCADE)
    direction=models.CharField(50)

    def __str__(self):
        return "%s domiciliary has ID as %s"%(self.name, self.id_domc)


class product(models.Model):
    id_product=models.SmallIntegerField(primary_key=True)
    id_cart=models.SmallIntegerField(null=False)
    product_name=models.SmallIntegerField(null=False)
    unit_price=models.IntegerField(null=False)
    id_admin=models.ForeignKey(
    admin,
    on_delete=models.CASCADE
    )
    def __str__(self):
        return "%s has ID product as %s"%(self.product_name,self.id_product)

class shopping_car(mod)


class gummy(models.Model):
    id_product=models.OneToOneField(product, on_delete=CASCADE)
    flavor= models.CharField(50)
    type=models.CharField(50)

    def __str__(self):
        return "%s is a gummy with a(n) %s flavor" %(self.id_product,self.flavor)

class chocolate(models.Model):
    id_product=models.OneToOneField(product, on_delete=CASCADE)
    flavor= models.CharField(50)
    type=models.CharField(50)

    def __str__(self):
        return "%s is a chocolate with a(n) %s flavor" %(self.id_product,self.flavor)

class flowers(models.Model):
    id_product=models.OneToOneField(product, on_delete=CASCADE)
    weight= models.SmallIntegerField(null=False)
    price_of_bouquet=models.IntegerField(null=False)
    amount_of_flowers=models.SmallIntegerField(null=False)

    def __str__(self):
        return "%s is a bouquet of flowers that cost %s" %(self.id_product,self.price_of_bouquet)

class box_of_chocolates(models.Model):
    id_product=models.ManyToManyField(
    product,
    on_delete=CASCADE,
    primary_key=True
    )
    class_=models.CharField(30)
    weight=models.SmallIntegerField(null=False)
    expedition_date=models.DateTimeField(default=timezone.now)
    expiration_date=models.DateTimeField(default=timezone.now)
    total_price= models.IntegerField(null=False)
    number_of_units=models.SmallIntegerField(null=False)

    def __str__(self):
        return "The product %s is a chocolate box of the class %s"(self.id_product,self.class_)

class box_of_gummies(models.Model):
    id_product=models.ManyToManyField(
    product,
    on_delete=CASCADE,
    primary_key=True
    )
    class_=models.CharField(30)
    weight=models.SmallIntegerField(null=False)
    expedition_date=models.DateTimeField(default=timezone.now)
    expiration_date=models.DateTimeField(default=timezone.now)
    total_price= models.IntegerField(null=False)
    number_of_units=models.SmallIntegerField(null=False)

    def __str__(self):
        return "The product %s is a gummy box of the class %s"(self.id_product,self.class_)

class  arrag_of_gummies(models.Model):
    id_product=models.ManyToManyField(
    product,
    on_delete=CASCADE,
    primary_key=True
    )
    arrag_price=models.IntegerField(null=False)
    theme=models.CharField(50)
    expedition_date=models.DateTimeField(default=timezone.now)
    weight=models.SmallIntegerField(null=False)
    package=models.CharField(50)

    def __str__(self):
        return
