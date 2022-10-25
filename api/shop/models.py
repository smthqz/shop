from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField()
    price = models.IntegerField(blank=True, null=True)
    image = models.ImageField(blank=True, upload_to='images/')
    description = models.TextField(blank=True)
    articul = models.CharField(max_length=16, blank=True)
    subcategoryId = models.ForeignKey('SubCategory', on_delete=models.PROTECT, null=True)
    category_id = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

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
      return self.name

