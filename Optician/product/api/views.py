from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import status, permissions

from product.models import Product, ProductVersion
from .serializers import  ProductSerializer, ProductversionSerializers
from django_filters.rest_framework import DjangoFilterBackend


class ProductAPIView(APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            obj = Product.objects.get(pk=kwargs.get('pk'))
            serializer = self.serializer_class(obj)

        else:
            allProducts = Product.objects.all()
            
            serializer = self.serializer_class(allProducts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductVersionAPIView(APIView):
    serializer_class = ProductversionSerializers

    def get(self, request, *args, **kwargs):
        if kwargs.get('product_id'):
            obj = ProductVersion.objects.filter(product_id=kwargs.get('product_id'))
            stat = status.HTTP_200_OK
            result = self.serializer_class(obj, many=True).data
            if kwargs.get('pk'):
                obj = ProductVersion.objects.get(pk=kwargs.get('pk'))
                result = self.serializer_class(obj).data

        else:
            stat = status.HTTP_404_NOT_FOUND
            result = {'error': 'Product not found'}

        return Response(result,status=stat)

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'manufacturer']
