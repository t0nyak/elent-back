from django.contrib import admin
from django import forms
from .models import CartItem, Cart, Category, Product
from api.models import Image


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'price_ht')


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')


class ProductAdmin(admin.ModelAdmin):
    #form = ProductModelForm
    list_display = ('name', 'category', 'price')


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Product, ProductAdmin)
