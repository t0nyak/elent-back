from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework import generics
from . import models
from .serializers import ProductSerializer, CategorySerializer, CartSerializer


# Just wraps a simple HTTP Response to a JSON Response
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def index(request):
    return HttpResponse("&lt;h3&gt;Welcome to Trees ONG Blog API v0.1&lt;/h3&gt;")


@api_view(['GET'])
def products(request):
    products = models.Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JSONResponse(serializer.data)


@api_view(['GET'])
def categories(request):
    categories = models.Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return JSONResponse(serializer.data)


@api_view(['GET'])
def carts(request):
    carts = models.Cart.objects.all()
    serializer = CartSerializer(carts, many=True)
    return JSONResponse(serializer.data)


class CartList(generics.ListAPIView):
    queryset = models.Cart.objects.all()
    serializer_class = CartSerializer


class CartDetail(generics.RetrieveAPIView):
    queryset = models.Cart.objects.all()
    serializer_class = CartSerializer
