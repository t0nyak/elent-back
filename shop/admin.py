from django.contrib import admin
from .models import CartItem, Cart, Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name'


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'price_ht')


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')


class Product(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')


# Register your models here.
admin.site.register(Category)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Product)
