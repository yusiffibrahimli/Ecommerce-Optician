from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from product.models import Product
from blog.models import Blog
from .forms import SubscriberForm
from django.db.models import Q

# Create your views here.

def about(request):
    # Your view logic here
    return render(request, 'about-us.html')

def index(request):
    return render(request, 'index.html') 

class IndexView(ListView):
    model= Product
    paginate_by = 4
    template_name ='index.html'
    context_object_name='product'
    def get_queryset(self):
        cat=self.request.GET.get('categories')
        if cat:
            return Product.objects.filter(category__name=cat)
        else:
            return Product.objects.all()
    def get_context_data(self, **kwargs,):
        context= super().get_context_data(**kwargs)
        context['blogs']=Blog.objects.order_by('created')
        context['products']=Product.objects.order_by('name')
        return context

class SearchView(ListView):
    model = Product
    template_name = 'search.html'
    context_object_name = 'products'

    def get_queryset(self):
        product = self.request.GET.get('q')
        if product:
            multiple = Product.objects.filter(Q(name__icontains=product))

        else:
            multiple = Product.objects.all()

        return multiple

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for subscribing!')
            return redirect('subscribe')  
    else:
        form = SubscriberForm()
    return render(request, 'base.html', {'form': form})