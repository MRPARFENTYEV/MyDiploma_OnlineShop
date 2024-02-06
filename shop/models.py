from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    mobile_phone = models.IntegerField()
    email = models.EmailField(max_length=320, unique=True)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
