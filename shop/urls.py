from django.urls import path, include
from . import views
from rest_framework import routers, viewsets
from .models import Category, Cart, Product, Socio, CartItem
from .serializers import CartSerializer, CategorySerializer, CartItemSerializer, ProductSerializer


# ViewSets define the view behavior.
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'carts', CartViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('carts/', views.CartList.as_view()),
    path('carts/<str:pk>', views.CartDetail.as_view()),
    path('products/', views.products),
    path('categories/', views.categories)
]