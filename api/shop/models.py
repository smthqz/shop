from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.TextField()
    price = models.IntegerField(blank=True, null=True)
    image = models.ImageField(blank=True, upload_to='images/')
    description = models.TextField(blank=True)
    articul = models.CharField(max_length=16, blank=True)
    subcategoryId = models.ForeignKey('SubCategory', on_delete=models.PROTECT, null=True)
    category_id = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    isBoolean = models.BooleanField(default=True, verbose_name="В наличие")


    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    itemId = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
      return str(self.id)

class Order(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    date_created = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    date_payment = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    date_modification = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    comment = models.TextField(blank=True, null=True)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self._id)

class Cart(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return str(self._id)

