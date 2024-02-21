from rest_framework import serializers
from rest_framework.relations import StringRelatedField

# from shop.models import Shop, Category


from shop.models import Client, Category, Product, Shop, ProductInfo, Parameter, Order, ShopCategory


# class ShopCategorySerializer(serializers.ModelSerializer):# пока не используется
#     # category = serializers.StringRelatedField(many=True, read_only=True)
#
#     class Meta:
#         model = ShopCategory
#         fields = "__all__"

class ShopCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopCategory
        fields =['shop','category']


class CategorySerializer(serializers.ModelSerializer):
    shops = ShopCategorySerializer(many=True)
    # shops = serializers.StringRelatedField(many=True, read_only=True)
    # product = ProductSerializer(many=True)
    class Meta:
        model = Category
        # exclude = ('id',)
        fields = "__all__"
    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        goods = validated_data.pop('goods')

        # создаем категорию по ее параметрам
        category = super().create(validated_data)# продумать момент названия получше

        for categ in goods:

            ShopCategory.objects.create(category=category, shop=categ['shop'])

        return category


class ShopSerializer(serializers.ModelSerializer):
    # тут надо исправить на категории
    # category = StringRelatedField(many=True, read_only=True)
    # category = ShopCategorySerializer(many=True)  'Shop' object has no attribute 'category'.
    # category = RecursiveSerializer(many=True, read_only=True)
    class Meta:
        model = Shop
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        # fields = ['id', 'name', 'email']

#
class ProductSerializer(serializers.ModelSerializer):
    # categories = serializers.HyperlinkedRelatedField(many=True, read_only=True,  view_name='product-detail')# не работает
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
        # fields =('name','category')
        # exclude = ('id',)


    # def create(self, validated_data):
    #     # достаем связанные данные для других таблиц
    #     categories = validated_data.pop('categories')
    #
    #     # создаем категорию по ее параметрам
    #     category = super().create(validated_data)# продумать момент названия получше
    #
    #     for categ in categories:
    #
    #         Product.objects.create(categories=categories, name=categ['name'], shops=categ['shops'])
    #
    #     return category


    # def update(self, instance, validated_data):
    #     # достаем связанные данные для других таблиц
    #     positions = validated_data.pop('positions')
    #     stock = super().update(instance, validated_data)# непонятный момент - найти его в документации
    #
    #     for position in positions:
    #         object, created = StockProduct.objects.update_or_create(
    #             stock=stock,
    #             product=position['product'],
    #             defaults={'stock': stock, 'product': position['product'], 'quantity': position['quantity'],
    #                       'price': position['price']}
    #         )
    #
    #     return stock

class ProductInfoSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    # product = serializers.StringRelatedField(many=True)
    # product = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # product = ProductSerializer(many=True)
    # product = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='product-detail'
    # ) !! 'Product' object is not iterable

    class Meta:
        model = ProductInfo
        # fields = "__all__"
        exclude = ('id', )
class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = "__all__"
class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"
# class ShopSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Shop
#         fields = "__all__"

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = "__all__"