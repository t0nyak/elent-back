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
    created_on = serializers.DateTimeField(format="%d %B, %Y")

    class Meta:
        model = models.Post
        fields = '__all__'
        depth = 1
