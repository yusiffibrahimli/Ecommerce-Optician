from django.contrib import admin
from .models import WishList, Basket, BasketItem

# Register your models here.

admin.site.register(WishList)
admin.site.register(Basket)
admin.site.register(BasketItem)