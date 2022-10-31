from django.contrib import admin

# Register your models here.
from shop.models import Product, Category, SubCategory, Cart, Order

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Cart)
admin.site.register(Order)





