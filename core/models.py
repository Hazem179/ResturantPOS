from email.policy import default
from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name

SIZES = (('1','Medium'),('2','Large'))
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    size = models.CharField(max_length=2, null=True, choices=SIZES)
    def __str__(self):
        return self.name


TYPES = (('1','Place'),('2','Delivery'))
class Invioce(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True,blank =True)
    type = models.CharField(max_length=2, null=True, choices=TYPES)
    discount = models.FloatField(default=0)
    total = models.FloatField(default=0)
    delivery_price = models.FloatField(default=0)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return str(self.type)

class Order(models.Model):
    invioce = models.ForeignKey(Invioce, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return str(self.product)