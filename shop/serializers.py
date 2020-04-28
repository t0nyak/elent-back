from rest_framework import serializers
from django.conf import settings
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
    images = serializers.SerializerMethodField('get_image_url')
    category = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )

    def get_image_url(self, obj):
        return {settings.MEDIA_ROOT + '/' + x.image.url for x in obj.images.all()}

    class Meta:
        model = models.Product
        fields = ('__all__')
