from django.db import models
from django.urls import reverse

# Н
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',on_delete= models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # def get_absolute_url(self):
    #     return reverse('myshop:products')


    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    mobile_phone = models.IntegerField()
    email = models.EmailField(max_length=320, unique=True)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name, self.surname

# class ShoppingCart(models.Model):
#     product = models.ForeignKey(Product, related_name='products',on_delete= models.CASCADE)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.PositiveIntegerField(default=1)


