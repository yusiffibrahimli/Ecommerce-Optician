from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import status, permissions

from product.models import ProductVersion
from .serializers import WishListSerializer, BasketSerializer
from order.models import WishList, Basket, BasketItem
from django_filters.rest_framework import DjangoFilterBackend

class WishListAPIView(APIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer

    http_method_names = ['get', 'post', 'delete']

    def get(self, request, *args, **kwargs):
        wishlist =  WishList.objects.filter(user=self.request.user).first()
        serializer = self.serializer_class(wishlist)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        product = request.data.get('product')
        version = ProductVersion.objects.filter(pk=product).first()

        if version and self.request.user.is_authenticated:
            wishlist =  WishList.objects.filter(user=self.request.user.pk).first()
            if wishlist:
                wishlist.product.add(version)
            else:
                wishlist = WishList.objects.create(user=self.request.user)
                wishlist.product.add(version)
            message = {'success': True, 'message':"Product added to your wishlist"}
            return Response({'message': message}, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        product = request.data.get('product')
        version = ProductVersion.objects.filter(pk=product).first()
        if version and self.request.is_authenticated:
            wishlist =  WishList.objects.filter(user=self.request.user).first()

            if wishlist:
                wishlist.products.remove(version)
                message = {'success': True, 'message':"Product removed to your wishlist"}
                return Response(message, status=status.HTTP_200_OK)
            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class BasketAPIView(ListAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    http_method_names = ['get', 'post', 'delete']

    def get(self, request, *args, **kwargs):
        basket = Basket.objects.filter(user=self.request.user).first()
        serializer = self.serializer_class(basket)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        product = request.data.get('product')
        quantity = request.data.get('quantity')
        version = ProductVersion.objects.filter(pk=product).first()
        if version and self.is_authenticated:
            basket = Basket.objects.filter(user=self.request.user).first()

            if basket:
                basket_item = basket.items.filter(product=version).first()
                if basket_item:
                    basket_item.quantity += int(quantity)
                    basket_item.save()
                else:
                    basket_item = basket.items.create(user = self.request.user , product=version, quantity=quantity)

        else:
            basket = Basket.objects.create(user=self.request.user)
            basket_item = basket.items.create(user = self.request.user , product=version, quantity=quantity)
        
        message = {'success': True, 'message':"Product added to your basket"}
        return Response(message, status=status.HTTP_201_CREATED)
    
    def delete(self, request, *args, **kwargs):
        product = request.data.get('product')
        version = ProductVersion.objects.filter(pk=product).first()
        if version and self.request.is_authenticated:
            basket =  Basket.objects.filter(user=self.request.user).first()

            if basket:
                basket_item = basket.items.filter(product=version).first()
                if basket_item:
                    basket_item.delete()
                    message = {'success': True, 'message':"Product removed to your basket"}
                    return Response(message, status=status.HTTP_200_OK)
                
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)           
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)