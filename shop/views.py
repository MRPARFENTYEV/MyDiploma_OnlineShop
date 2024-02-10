from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet

from shop.models import Client,Category,Product
from shop.serializers import ClientSerializer, CategorySerializer,ProductSerializer


# Create your views here.
# Представления:
def index(request) -> HttpResponse:
    content: dict = {'title': 'Home',
                     'content': 'Главная страница'
    }
    return render(request,'index.html', content)
def about(request)-> HttpResponse:
    return HttpResponse('About')
class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
