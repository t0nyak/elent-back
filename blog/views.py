
from rest_framework import generics
from . import models
from .serializers import AuthorSerializer, CategorySerializer, PostSerializer


class LastPostsList(generics.ListAPIView):
    queryset = models.Post.objects.filter(status=1)[:3]
    serializer_class = PostSerializer
