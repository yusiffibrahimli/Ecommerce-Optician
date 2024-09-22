from rest_framework import serializers

from product.models import Product, ProductVersion, Category, Manufacturer, Color, Image


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
        ]

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = [
            'name',
        ]

class ProductversionSerializers(serializers.ModelSerializer):

    class Meta:
        model=ProductVersion
        fields=[
            'id',
            'cover_image',
        ]

    # def get_detail_url(self,obj):
    #     return obj.get_absolute_url()

class ProductSerializer(serializers.ModelSerializer):
    # total_quantity = serializers.SerializerMethodField()
    # main_version = serializers.SerializerMethodField()
    versions =  ProductversionSerializers(many=True)
    category = CategorySerializer()
    manufacturer = ManufacturerSerializer()
    detail_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['name', 'in_sale', 'price', 'old_price', 'versions','category','manufacturer', 'detail_url']

    def get_detail_url(self,obj):
        return obj.get_absolute_url()

    # def get_total_quantity(self, obj):
    #     return obj.total_quantity
    
    # def get_main_version(self, obj):
    #     return ProductversionSerializers(obj.main_version).data
    
    # def get_versions(self, obj):
    #     queryset = obj.versions.all()
    #     return ProductversionSerializers(queryset, many=True).data