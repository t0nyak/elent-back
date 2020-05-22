from rest_framework import serializers
from django.conf import settings
from . import models


PROJECT_UNITS = (
    (0, 'hectareas'),
    (1, 'árboles'),
    (2, 'toneladas'),
    (3, 'euros')
)


class ProjectSerializer(serializers.ModelSerializer):
    unit = serializers.SerializerMethodField('get_unit_name')
    image = serializers.SerializerMethodField('get_image_url')

    def get_unit_name(self, obj):
        return PROJECT_UNITS[obj.unit][1]

    def get_image_url(self, obj):
        return obj.image.image.url

    class Meta:
        model = models.Project
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self):
        return self.image.url

    class Meta:
        model = models.Image
        fields = '__all__'
