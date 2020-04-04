from django.urls import path, include
from . import views
from rest_framework import routers, viewsets
from .serializers import AuthorSerializer, CategorySerializer, PostSerializer
from .models import Author, Category, Post


# ViewSets define the view behavior.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', views.PostList.as_view()),
    path('posts/<str:pk>', views.PostDetail.as_view()),
    path('authors/', views.authors),
    path('categories/', views.categories)
]
