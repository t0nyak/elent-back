from rest_framework import serializers

from . import models
from api.serializers import ImageSerializer


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Author
        fields = '__all__'


class BlogCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BlogCategory
        fields = '__all__'


class ComplexBlogCategorySerializer(serializers.Serializer):
    uuid = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=50)
    posts = serializers.IntegerField()

    def create(self, validated_data):
        return models.BlogCategory(name=validated_data['name'])

    def update(self, instance, validated_data):
        instance.uuid = validated_data.get('uuid', instance.uuid)
        instance.name = validated_data.get('name', instance.name)
        return instance


class PostSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format="%d %B, %Y")
    images = ImageSerializer

    class Meta:
        model = models.Post
        fields = '__all__'
        depth = 1
