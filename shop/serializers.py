from rest_framework import serializers

# from shop.models import Shop, Category


from shop.models import Client, Category, Product, Shop, ProductInfo, Parameter, Order, ShopCategory


class ShopCategorySerializer(serializers.ModelSerializer):# пока не используется
    class Meta:
        model = ShopCategory
        fields = "__all__"
class ShopSerializer(serializers.ModelSerializer):
    # тут надо исправить на категории
    class Meta:
        model = Shop
        fields = "__all__"
class CategorySerializer(serializers.ModelSerializer):
    shops = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Category
        fields = "__all__"






class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'email']

#
class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.HyperlinkedRelatedField(many=True, read_only=True,  view_name='product-detail')# не работает

    class Meta:
        model = Product
        fields = "__all__"
class ProductInfoSerializer(serializers.ModelSerializer):
    # product = serializers.StringRelatedField(many=True, read_only=True)
    # product = serializers.PrimaryKeyRelatedField(many=True,read_only=True)                                      )
    # product = ProductSerializer(many=True)
    # product = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='product-detail'
    # ) !! 'Product' object is not iterable

    class Meta:
        model = ProductInfo
        fields = "__all__"
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