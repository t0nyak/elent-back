from rest_framework import serializers
from . import models

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Author
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
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
        model = models.Post
        fields = ('__all__')