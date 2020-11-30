from django.contrib import admin

# Register your models here.
from .models import Product, OrderItem, Order

admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)