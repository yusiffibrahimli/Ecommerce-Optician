from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from order.models import WishList, Basket

# Create your views here.

class BasketView(LoginRequiredMixin, ListView):
    model = Basket
    template_name = 'cart.html'
    context_object_name = 'basket'

    def get_queryset(self):
        return Basket.objects.filter(user=self.request.user).first()


def checkout(request):
    # Your view logic here
    return render(request, 'checkout.html')

class WishlistView(LoginRequiredMixin, ListView):
    model = WishList
    template_name = 'wishlist.html'
    context_object_name = 'wishlist'


    def get_queryset(self):
        return WishList.objects.filter(user=self.request.user).first()