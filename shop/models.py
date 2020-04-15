from django.db import models
from api.models import Image
import uuid

from datetime import datetime


# Create your models here.
from api.models import Socio


class Category(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name


class Product(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    price = models.FloatField()

    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    images = models.ManyToManyField(Image)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.name


class Cart(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=datetime.now)

    user = models.ForeignKey(Socio, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user + ' - ' + self.created_at


class CartItem(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    quantity = models.IntegerField(default=1)
    price_ht = models.FloatField(blank=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return self.product + " - x" + self.quantity