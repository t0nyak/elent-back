from rest_framework import serializers
from . import models


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = ('__all__')


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CartItem
        fields = ('__all__')


class CartSerializer(serializers.ModelSerializer):
    authors = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )
    categories = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = models.Cart
        fields = ('__all__')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = ('__all__')
