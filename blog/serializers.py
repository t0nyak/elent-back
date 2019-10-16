from rest_framework import serializers
from .models import Author, Category, Post

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('__all__')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('__all__')


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
        model = Post
        fields = ('__all__')