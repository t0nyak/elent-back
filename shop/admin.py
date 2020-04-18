from django.contrib import admin
from .models import CartItem, Cart, Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name'


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'price_ht')


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Product, ProductAdmin)
