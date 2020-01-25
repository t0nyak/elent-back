from rest_framework import serializers
from . import models


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        #fields = ('uuid', 'title', 'unit', 'description', 'visible', 'got', 'goal', 'created_on')
        fields = '__all__'
