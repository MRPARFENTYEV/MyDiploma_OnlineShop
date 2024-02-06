from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet

from shop.models import Client
from shop.serializers import ClientSerializer


# Create your views here.


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
