from django.contrib import admin

# Register your models here.
 
from . models import Product, Category, Manufacturer, Color, ProductVersion, Image
 
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Color)
admin.site.register(ProductVersion)
admin.site.register(Image)