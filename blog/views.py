from rest_framework import generics
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from . import models
from .serializers import PostSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class LastPostsList(generics.ListAPIView):
    queryset = models.Post.objects.filter(status=1)[:3]
    serializer_class = PostSerializer
