from django.core.validators import MinValueValidator
from django.db import models
from django_rest_passwordreset.tokens import get_token_generator
from django.urls import reverse

class Shop(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    url = models.URLField(verbose_name='Ссылка', null=True, blank=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    shops = models.ManyToManyField(Shop, related_name='shops')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
class ShopCategory(models.Model):

    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE, related_name='goods',)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE, related_name='goods')


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='categories',on_delete= models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    # slug = models.SlugField(max_length=200, db_index=True, unique=True)
    # image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    # description = models.TextField(blank=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    # stock = models.PositiveIntegerField()
    # available = models.BooleanField(default=True)
    # created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


    def __str__(self):
        return self.name

class ProductInfo(models.Model):
    product = models.ForeignKey(Product,related_name='products',on_delete= models.CASCADE)
    # могут быть проблемы
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(
            max_digits=18,
            decimal_places=2,
            validators=[MinValueValidator(0)],
        )
class Parameter(models.Model):
    name = models.CharField(max_length=200, db_index=True)

class ProductParameter(models.Model):
    product_info = models.ForeignKey(ProductInfo,related_name='ProductInfoes',on_delete= models.CASCADE)
    parameter = models.ForeignKey(Parameter,related_name='parameters',on_delete= models.CASCADE)
    value = models.CharField(max_length=20)

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

class Order(models.Model):
    client = models.ForeignKey(Client, related_name='clients',on_delete= models.CASCADE)
    dt = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
# готов ли заказ?
'''________________________________________________________________________'''
# class ConfirmEmailToken(models.Model):
#     class Meta:
#         verbose_name = 'Токен подтверждения Email'
#         verbose_name_plural = 'Токены подтверждения Email'
# 
#     @staticmethod
#     def generate_key():
#         """ generates a pseudo random code using os.urandom and binascii.hexlify """
#         return get_token_generator().generate_token()
# 
#     user = models.ForeignKey(
#         Client,
#         related_name='confirm_email_tokens',
#         on_delete=models.CASCADE,
#         verbose_name=_("The User which is associated to this password reset token")
#     )
# 
#     created_at = models.DateTimeField(
#         auto_now_add=True,
#         verbose_name=_("When was this token generated")
#     )
# 
#     # Key field, though it is not the primary key of the model
#     key = models.CharField(
#         _("Key"),
#         max_length=64,
#         db_index=True,
#         unique=True
#     )
# 
#     def save(self, *args, **kwargs):
#         if not self.key:
#             self.key = self.generate_key()
#         return super(ConfirmEmailToken, self).save(*args, **kwargs)
# 
#     def __str__(self):
#         return "Password reset token for user {user}".format(user=self.user)


# class Shop(models.Model):
#     name = models.CharField(max_length=200, db_index=True)
#     url = models.SlugField(max_length=200, unique=True)
#
# class Category(models.Model):
#     name = models.CharField(max_length=200, db_index=True)
#     shop = models.ManyToManyField(Shop)

    # class Meta:
    #     ordering = ('name',)
    #     verbose_name = 'Категория'
    #     verbose_name_plural = 'Категории'
    #
    # def __str__(self):
    #     return self.name

#
#
# class Product(models.Model):
#     category = models.ForeignKey(Category, related_name='categories',on_delete= models.CASCADE)
#     name = models.CharField(max_length=200, db_index=True)
#     image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
#     description = models.TextField(blank=True)
#
#
#     # def get_absolute_url(self):
#     #     return reverse('myshop:products')
#
#
#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'Товар'
#         verbose_name_plural = 'Товары'
#         index_together = (('id', 'slug'),)
#
#     def __str__(self):
#         return self.name
# class ProductInfo(models.Model):
#     product=models.ForeignKey(Product, related_name='products',on_delete= models.CASCADE)
#     shop = models.ForeignKey(Shop, related_name='shops',on_delete= models.CASCADE)
#     quantity=models.PositiveIntegerField(default=1)
#     price = models.DecimalField(
#         max_digits=18,
#         decimal_places=2,
#         validators=[MinValueValidator(0)],
#     )
#     available = models.BooleanField(default=True)
#
#
# class Client(models.Model):
#     name = models.CharField(max_length=25)
#     surname = models.CharField(max_length=25)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name, self.surname
#
#
# class Parameter(models.Model):
#     name = models.CharField(max_length=25)
#
# class ProductParameter(models.Model):
#     product_info = models.ForeignKey(ProductInfo, related_name='product_info',on_delete= models.CASCADE)
#     parameter = models.ForeignKey(Parameter,on_delete= models.CASCADE)
#     # value = don`t understand why do I need this one...
#
#
# class Order(models.Model):
#
#     client = models.ForeignKey(Client, related_name='clients',on_delete= models.CASCADE)
#     dt = models.DateTimeField(auto_now_add=True)
#     status = models.BooleanField(default=True) # готов ли заказ?
#
#
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, related_name='orders',on_delete= models.CASCADE)
#     product = models.ForeignKey(Product, related_name='products',on_delete= models.CASCADE)
#     shop = models.ForeignKey(Shop, related_name='shops',on_delete= models.CASCADE)
#     quontity = models.PositiveIntegerField(default=1)
#
#
#
# class Contact(models.Model):
#     user = models.ForeignKey(Client, verbose_name='Пользователь',
#                              related_name='contacts', blank=True,
#                              on_delete=models.CASCADE)
#
#     city = models.CharField(max_length=50, verbose_name='Город')
#     street = models.CharField(max_length=100, verbose_name='Улица')
#     house = models.CharField(max_length=15, verbose_name='Дом', blank=True)
#     structure = models.CharField(max_length=15, verbose_name='Корпус', blank=True)
#     building = models.CharField(max_length=15, verbose_name='Строение', blank=True)
#     apartment = models.CharField(max_length=15, verbose_name='Квартира', blank=True)
#     phone = models.CharField(max_length=20, verbose_name='Телефон')
#
#     class Meta:
#         verbose_name = 'Контакты пользователя'
#         verbose_name_plural = "Список контактов пользователя"
#
#     def __str__(self):
#         return f'{self.city} {self.street} {self.house}'
#
#
# # class ShoppingCart(models.Model):
# #     product = models.ForeignKey(Product, related_name='products',on_delete= models.CASCADE)
# #     price = models.DecimalField(max_digits=10, decimal_places=2)
# #     quantity = models.PositiveIntegerField(default=1)
#
#
