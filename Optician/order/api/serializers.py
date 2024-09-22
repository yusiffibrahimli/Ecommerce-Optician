from rest_framework import serializers
from order.models import WishList, Basket, BasketItem
from django.contrib.auth.models import User
from product.api.serializers import ProductversionSerializers

class WishListSerializer(serializers.ModelSerializer):
    product = ProductversionSerializers(many=True)

    class Meta:
        model = WishList
        fields = ['product', 'user', ]

class BasketItemSerializer(serializers.ModelSerializer):
    product = ProductversionSerializers()

    class Meta:
        model = BasketItem
        fields = ['user', 'quantity', 'product']

class BasketSerializer(serializers.ModelSerializer):
    items = BasketItemSerializer(many=True) 

    class Meta:
        model = Basket
        fields = ['user', 'items']
