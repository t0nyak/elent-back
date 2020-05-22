from django.urls import path, include
from . import views
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import routers, viewsets
from .serializers import AuthorSerializer, BlogCategorySerializer, PostSerializer, ComplexBlogCategorySerializer
from .models import Author, BlogCategory, Post


# ViewSets define the view behavior.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(status=1)
    serializer_class = PostSerializer

    @action(detail=False, methods=['get'])
    def latest_posts(self, request, pk=None):
        last_posts = Post.objects.filter(status=1)[:3]
        serializer = self.get_serializer(last_posts, many=True)
        return Response(serializer.data)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = ComplexBlogCategorySerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
