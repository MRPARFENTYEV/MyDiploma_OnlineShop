from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet

from shop.models import Client, Category, Product, Shop, ProductInfo, Parameter, Order
from shop.serializers import (ClientSerializer, CategorySerializer, ProductSerializer, ShopSerializer,
                              ProductInfoSerializer, ParameterSerializer, OrderSerializer)


# from shop.models import Shop , Category
# from shop.serializers import ShopSerializer,CategorySerializer
# class ShopViewSet(ModelViewSet):
#     queryset = Shop.objects.all()
#     serializer_class = ShopSerializer

class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductInfoViewSet(ModelViewSet):
    queryset = ProductInfo.objects.all()
    serializer_class = ProductInfoSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


#
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ParameterViewSet(ModelViewSet):
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer