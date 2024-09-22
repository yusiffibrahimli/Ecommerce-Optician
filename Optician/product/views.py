from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, ProductVersion, Category, Manufacturer, Color, Image

from django.core.paginator import Paginator

class ProductView(ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'
    paginate_by = 2  # Hər səhifədə 2 məhsul

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['manufacturers'] = Manufacturer.objects.all()
        context['colors'] = Color.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'single-product.html'
    context_object_name = 'product_detail'

    def get_object(self):
       
        return  ProductVersion.objects.filter(pk=self.kwargs['pk']).first()
      

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(versions = self.get_object())
        
        product_versions = product.versions.all()  
       
        product_colors = []
        for version in product_versions:
            product_colors.append(version.color)       

        context['colors'] = product_colors
        context['images'] = self.get_object().image.all()
        context['manufacturer'] = product.manufacturer 
        context['in_sale'] = product.in_sale

        return context